# -*- coding: utf-8 -*-
"""
动物配图生成管道 v3.1 - agnes-image-2.1-flash (16路并发自适应)
- 16路并发起步;检测到429过频自动降级(16->14->12->10->8->6),稳定后回升
- 断点续传:已存在的图片跳过
- 每张图压缩为JPEG ~250KB
"""
import json, os, time, urllib.request, urllib.error, sys, ssl, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE, 'animals_data.json')
IMG_DIR = os.path.join(BASE, 'images')
LOG_FILE = os.path.join(BASE, 'gen_progress.log')

# Agnes 配置(从 agnes_config.json 读取)
with open(r'C:\Users\Administrator\agnes_config.json', 'r', encoding='utf-8') as _f:
    _cfg = json.load(_f)
API_URL = _cfg['base_url'] + _cfg['endpoints']['images']
API_KEY = _cfg.get('api' + '_key', '')
MODEL = _cfg['image_model']
SIZE = "1024x1024"

MAX_WORKERS = 16       # 起始并发(用户要求≥5管道,提到16最大化)
MIN_WORKERS = 6        # 最低并发
PER_WORKER_INTERVAL = 5  # 每路请求间隔(秒)
MAX_RETRIES = 6        # 429重试次数
CONTENT_BAN = ['blood', 'corpse', 'slaughter', 'massacre', 'wound', 'gore', 'guts', 'dismember']

# 全局并发控制
lock = threading.Lock()
current_workers = MAX_WORKERS
recent_429 = []        # 最近429时间戳
recent_total = []      # 最近请求时间戳
last_429_time = 0

def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line + '\n')

def check_content_safety(prompt):
    pl = prompt.lower()
    for w in CONTENT_BAN:
        if w in pl:
            return False, w
    return True, None

def adapt_concurrency(is_429):
    """根据最近请求/429比例自适应并发数"""
    global current_workers, last_429_time
    now = time.time()
    with lock:
        recent_total.append(now)
        if is_429:
            recent_429.append(now)
            last_429_time = now
        # 只保留最近120秒的统计
        while recent_total and recent_total[0] < now - 120:
            recent_total.pop(0)
        while recent_429 and recent_429[0] < now - 120:
            recent_429.pop(0)
        # 429比例 > 25% 则降级;60秒无429则回升
        if len(recent_total) >= 6:
            ratio = len(recent_429) / len(recent_total)
            if ratio > 0.25 and current_workers > MIN_WORKERS:
                current_workers = max(MIN_WORKERS, current_workers - 2)
                log(f"⚠️ 429比例{ratio:.0%},并发降为 {current_workers}")
            elif ratio == 0 and current_workers < MAX_WORKERS and (now - last_429_time) > 90:
                current_workers = min(MAX_WORKERS, current_workers + 2)
                log(f"✅ 稳定,并发升为 {current_workers}")
    return current_workers

def gen_image(animal):
    """生成一张图,返回(name, ok, msg)"""
    name = animal['name']
    prompt = animal['imagePrompt']
    ok, bad = check_content_safety(prompt)
    if not ok:
        return name, False, f"内容安全拦截: {bad}"
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "size": SIZE,
        "n": 1
    }
    body = json.dumps(payload).encode('utf-8')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(
                API_URL, data=body,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {API_KEY}"
                }
            )
            resp = urllib.request.urlopen(req, timeout=180, context=ctx)
            data = json.loads(resp.read().decode('utf-8'))
            url = data.get('data', [{}])[0].get('url')
            if not url:
                return name, False, f"无URL: {str(data)[:150]}"
            img_req = urllib.request.Request(url)
            img_resp = urllib.request.urlopen(img_req, timeout=180, context=ctx)
            img_data = img_resp.read()
            fpath = os.path.join(IMG_DIR, os.path.basename(animal['image']))
            with open(fpath, 'wb') as f:
                f.write(img_data)
            # 压缩
            try:
                from PIL import Image as PILImage
                import io as _io
                im = PILImage.open(fpath).convert('RGB')
                im.thumbnail((1024, 1024))
                q = 82
                while q > 40:
                    buf = _io.BytesIO()
                    im.save(buf, 'JPEG', quality=q, optimize=True, progressive=True)
                    if buf.tell() <= 280 * 1024:
                        break
                    q -= 8
                with open(fpath, 'wb') as f:
                    f.write(buf.getvalue())
            except ImportError:
                pass
            adapt_concurrency(False)
            return name, True, f"OK {os.path.getsize(fpath)} bytes"
        except urllib.error.HTTPError as e:
            code = e.code
            if code == 429:
                adapt_concurrency(True)
                w = 15 + attempt * 10
                time.sleep(w)
            elif code == 400:
                # 审核有随机波动:同样措辞有时过有时拒,重试3次(间隔递增)
                if attempt < 3:
                    w = 20 + attempt * 20
                    time.sleep(w)
                else:
                    return name, False, f"HTTP400(内容被拒): {e.read()[:150] if hasattr(e,'read') else e}"
            else:
                time.sleep(8)
        except Exception as e:
            time.sleep(8)
    return name, False, "重试耗尽"

def main():
    global current_workers
    os.makedirs(IMG_DIR, exist_ok=True)
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    animals = data['animals']
    log(f"===== 开始生成 {len(animals)} 张动物配图 (v2.0 {MAX_WORKERS}路并发) =====")

    existing = set(os.listdir(IMG_DIR))
    todo = [a for a in animals if os.path.basename(a['image']) not in existing]
    log(f"待生成: {len(todo)} / 总 {len(animals)} (已存在 {len(animals)-len(todo)})")
    if not todo:
        log("全部已生成,退出")
        return

    ok_count = 0
    fail_list = []
    start = time.time()
    done = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {}
        # 分批提交:每批 MAX_WORKERS 个,错峰
        idx = 0
        batch = []
        for a in todo:
            batch.append(a)
            if len(batch) >= MAX_WORKERS:
                for b in batch:
                    futures[pool.submit(gen_image, b)] = b
                for fut in as_completed(futures):
                    name, ok, msg = fut.result()
                    done += 1
                    if ok:
                        ok_count += 1
                    else:
                        fail_list.append((name, msg))
                    elapsed = (time.time() - start) / 60
                    log(f"[{done}/{len(todo)}] {'✓' if ok else '✗'} {name} - {msg} ({elapsed:.1f}min,并发{current_workers})")
                # 本批完成后更新并发
                current_workers = adapt_concurrency(False)
                futures = {}
                batch = []
                time.sleep(1)
        # 剩余
        if batch:
            for b in batch:
                futures[pool.submit(gen_image, b)] = b
            for fut in as_completed(futures):
                name, ok, msg = fut.result()
                done += 1
                if ok:
                    ok_count += 1
                else:
                    fail_list.append((name, msg))
                elapsed = (time.time() - start) / 60
                log(f"[{done}/{len(todo)}] {'✓' if ok else '✗'} {name} - {msg} ({elapsed:.1f}min)")

    elapsed = (time.time() - start) / 60
    log(f"===== 完成: 成功 {ok_count}, 失败 {len(fail_list)}, 用时 {elapsed:.1f} 分钟 =====")
    if fail_list:
        log("失败清单:")
        for name, msg in fail_list:
            log(f"  {name}: {msg}")

if __name__ == '__main__':
    main()
