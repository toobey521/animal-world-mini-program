# -*- coding: utf-8 -*-
"""最终合并: 225保留 + 各批次 + 子智能体 = 精确1000种
- 合并所有来源
- 去重(中文名/学名)
- 相似校验:同属最多2种
- 若超过1000,裁剪多余;若不足,报缺口
"""
import json, os, re, sys
from collections import Counter, defaultdict

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(PROJ, 'data_batches')

def load_json(fname):
    p = os.path.join(BATCH, fname)
    if not os.path.exists(p):
        return None
    try:
        with open(p, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"  ⚠️ {fname} 解析失败: {e}")
        return None

def load_py(fname, var):
    import importlib.util
    spec = importlib.util.spec_from_file_location(fname.replace('.py',''), os.path.join(BATCH, fname))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, var)

# ===== 1. 收集所有来源 =====
sources = []

# 保留225
kept = load_json('kept_300.json')
if kept:
    sources.append(('kept', kept))
    print(f"kept_300.json: {len(kept)}")

# 我自写的py批次
for f, var in [('batch6_extra.py','EXTRA'), ('batch7_mammals3.py','MAMMALS3')]:
    try:
        d = load_py(f, var)
        sources.append((f, d))
        print(f"{f}: {len(d)}")
    except Exception as e:
        print(f"  ⚠️ {f} 加载失败: {e}")

# 子智能体json批次
json_files = [
    'new_mammals.json', 'new_mammals2.json',
    'new_birds.json', 'new_birds2.json', 'new_birds3.json',
    'new_fish.json', 'new_fish2.json',
    'new_reptiles.json', 'new_reptiles2.json',
    'new_amphibians.json',
    'new_insects.json', 'new_insects2.json', 'new_insects3.json',
    'new_crustaceans_mollusks.json',
]
for f in json_files:
    d = load_json(f)
    if d is not None:
        sources.append((f, d))
        print(f"{f}: {len(d)}")

# ===== 2. 合并 + 去重 =====
all_animals = []
seen_names = set()
seen_sci = set()
dups = []

for src, data in sources:
    if not isinstance(data, list):
        continue
    for a in data:
        if not isinstance(a, dict) or 'name' not in a:
            continue
        name = a['name']
        sci = str(a.get('scientificName', '')).strip().lower()
        # 名称或学名重复则跳过
        if name in seen_names or (sci and sci in seen_sci):
            dups.append((src, name, sci))
            continue
        seen_names.add(name)
        if sci:
            seen_sci.add(sci)
        a.setdefault('category', '其他')
        a.setdefault('weight', '未知')
        a.setdefault('length', '未知')
        a.setdefault('emoji', '🐾')
        a.setdefault('imagePrompt', '')
        all_animals.append(a)

print(f"\n合并后: {len(all_animals)} 种 (跳过重复 {len(dups)})")
if dups:
    print("重复示例:", dups[:10])

# ===== 3. 分类统计 =====
cats = Counter(a['category'] for a in all_animals)
for c, n in cats.most_common():
    print(f"  {c}: {n}")

# ===== 4. 相似校验: 同属>2 =====
print("\n=== 同属>2 (需处理) ===")
genus = defaultdict(list)
for a in all_animals:
    parts = str(a.get('scientificName', '')).split()
    if parts:
        genus[parts[0]].append(a['name'])
over_genus = {g: n for g, n in genus.items() if len(n) > 2}
for g, names in sorted(over_genus.items(), key=lambda x: -len(x[1])):
    print(f"  {g} ({len(names)}): {names[:10]}")

# ===== 5. 保存全量 =====
out = os.path.join(PROJ, 'animals_merged.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(all_animals, f, ensure_ascii=False, indent=1)
print(f"\n已保存: {out} ({len(all_animals)}条)")
print(f"目标: 1000, 当前: {len(all_animals)}, 差额: {1000 - len(all_animals)}")
