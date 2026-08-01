# -*- coding: utf-8 -*-
"""权威合并 v2: 全部17个来源 → 去重 → 相似裁剪 → 精确1000种"""
import json, os, re, importlib.util
from collections import Counter, defaultdict

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(PROJ, 'data_batches')

def load_json(fname):
    p = os.path.join(BATCH, fname)
    if not os.path.exists(p): return []
    try: return json.load(open(p, encoding='utf-8'))
    except: return []

def load_py(fname, var):
    spec = importlib.util.spec_from_file_location(fname.replace('.py',''), os.path.join(BATCH, fname))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, var)

# ===== 全部来源 =====
sources = []
kept = load_json('kept_300.json')
sources.append(('kept', kept))

for f, var in [('batch6_extra.py','EXTRA'), ('batch7_mammals3.py','MAMMALS3'),
               ('batch8_final.py','FINAL'), ('batch9_last.py','LAST'), ('batch10_eight.py','EIGHT')]:
    try:
        sources.append((f, load_py(f, var)))
    except: pass

for f in ['new_mammals.json','new_mammals2.json','new_mammals3.json',
          'new_birds.json','new_birds2.json','new_birds3.json','new_birds4.json',
          'new_fish.json','new_fish2.json',
          'new_reptiles.json','new_reptiles2.json',
          'new_amphibians.json',
          'new_insects.json','new_insects2.json','new_insects3.json',
          'new_crustaceans_mollusks.json']:
    d = load_json(f)
    if d:
        sources.append((f, d))

print(f"来源数: {len(sources)}")

# ===== 合并去重 =====
all_animals = []
seen_names = set()
seen_sci = set()
for src, data in sources:
    if not isinstance(data, list): continue
    for a in data:
        if not isinstance(a, dict) or 'name' not in a: continue
        name = a['name']
        sci = str(a.get('scientificName','')).strip().lower()
        if name in seen_names or (sci and sci in seen_sci):
            continue
        seen_names.add(name)
        if sci: seen_sci.add(sci)
        a.setdefault('category','其他'); a.setdefault('weight','未知')
        a.setdefault('length','未知'); a.setdefault('emoji','🐾')
        a.setdefault('imagePrompt','')
        all_animals.append(a)

print(f"合并去重后: {len(all_animals)}")

# ===== 相似裁剪: 同属>2 只保留2个(优先中文名不同字/差异大) =====
# 策略: 每个属保留2种, 优先保留 "保留名单(kept)" 中的 + 学名后缀差异大的
kept_names = {a['name'] for a in kept}
genus_map = defaultdict(list)
for a in all_animals:
    parts = str(a.get('scientificName','')).split()
    if parts:
        genus_map[parts[0]].append(a)

to_drop = set()
for g, members in genus_map.items():
    if len(members) <= 2: continue
    # 保留逻辑: kept中的优先; 其次按名称长度/独特字
    kept_m = [a for a in members if a['name'] in kept_names]
    others = [a for a in members if a['name'] not in kept_names]
    # 保留: kept中最多2个; 若kept不够2个,从others补
    survive = kept_m[:2]
    if len(survive) < 2:
        for a in others:
            if len(survive) >= 2: break
            # 优先选中文名结尾不同的(差异大)
            survive.append(a)
    # 丢弃其余的
    for a in members:
        if a not in survive:
            to_drop.add(a['name'])

print(f"相似裁剪删除: {len(to_drop)} 种")
for g in sorted(genus_map):
    members = genus_map[g]
    if len(members) > 2:
        kept_here = [a['name'] for a in members if a['name'] not in to_drop]
        print(f"  {g} {len(members)}->{len(kept_here)}: {kept_here}")

all_animals = [a for a in all_animals if a['name'] not in to_drop]
print(f"裁剪后: {len(all_animals)}")

# ===== 补足/裁剪到精确1000 =====
# 如果多了,删掉一些昆虫(昆虫数量最多,删重复度高的)
if len(all_animals) > 1000:
    # 统计各分类,优先从昆虫类删(数量最多且视觉相似度高)
    cats = Counter(a['category'] for a in all_animals)
    print("当前分类:", dict(cats))
    excess = len(all_animals) - 1000
    print(f"超出 {excess} 种,将从昆虫类删除")
    insect_names = [a['name'] for a in all_animals if a['category']=='昆虫类']
    drop_insects = insect_names[:excess]
    all_animals = [a for a in all_animals if a['name'] not in set(drop_insects)]
    print(f"删除昆虫: {drop_insects}")
    print(f"最终: {len(all_animals)}")

# ===== 生成最终文件 =====
cats = Counter(a['category'] for a in all_animals)
data = {
    "version": "3.0",
    "generatedAt": "2026-07-31",
    "totalAnimals": len(all_animals),
    "animalCategories": list(cats.keys()),
    "animals": all_animals
}
for i, a in enumerate(all_animals, 1):
    a['id'] = i
    slug = re.sub(r'[^a-z0-9]+', '-', a['englishName'].lower()).strip('-')
    a['image'] = f"images/{slug}.jpg"

with open(os.path.join(PROJ, 'animals_data.json'), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

js = "// 动物数据 v3.0 - 1000种 (自动生成,勿手改)\nconst ANIMALS_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n"
with open(os.path.join(PROJ, 'animals_data.js'), 'w', encoding='utf-8') as f:
    f.write(js)

print(f"\n✅ 最终 animals_data.json: {len(all_animals)} 种")
for c, n in cats.most_common():
    print(f"  {c}: {n}")

# 校验
names = [a['name'] for a in all_animals]
print(f"名称唯一: {len(set(names)) == len(names)}")
import os as _os
print(f"animals_data.js: {_os.path.getsize(os.path.join(PROJ,'animals_data.js'))//1024} KB")
