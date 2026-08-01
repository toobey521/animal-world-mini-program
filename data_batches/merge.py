# -*- coding: utf-8 -*-
"""合并5个批次数据 -> animals_data.json + 生成图片文件名映射"""
import importlib.util, json, os, re, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(BASE)

def load(fname, var):
    spec = importlib.util.spec_from_file_location(fname.replace('.py', ''), os.path.join(BASE, fname))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, var)

batches = [
    ('batch1_mammals.py', 'MAMMALS'),
    ('batch2_birds.py', 'BIRDS'),
    ('batch3_fish.py', 'FISH'),
    ('batch4_reptiles.py', 'REPTILES'),
    ('batch5_others.py', 'AMPHIBIANS'),
    ('batch5_others.py', 'INSECTS'),
    ('batch5_others.py', 'CRUSTACEANS'),
    ('batch5_others.py', 'MOLLUSKS'),
]

def safe_name(name):
    """中文名 -> 拼音文件名。用unicode转拼音太难,直接用索引+英文名slug"""
    return None

def slugify_english(english_name):
    s = english_name.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    s = re.sub(r'[-]+', '-', s)
    return s

all_animals = []
seen = set()
for fname, var in batches:
    data = load(fname, var)
    for a in data:
        if a['name'] in seen:
            print('WARN 重复名称:', a['name'])
            continue
        seen.add(a['name'])
        # 生成图片文件名: 拼音化中文名
        img = slugify_english(a['englishName'])
        a['id'] = len(all_animals) + 1
        a['image'] = f"images/{img}.jpg"
        a.pop('imagePlaceholder', None)
        all_animals.append(a)

print('总动物数:', len(all_animals))

# 分类统计
from collections import Counter
cats = Counter(a['category'] for a in all_animals)
for c, n in cats.items():
    print(f'  {c}: {n}')

# 生成 animals_data.json
data = {
    "version": "2.0",
    "generatedAt": "2026-07-31",
    "totalAnimals": len(all_animals),
    "animalCategories": list(cats.keys()),
    "animals": all_animals
}
out = os.path.join(PROJ, 'animals_data.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('已写入:', out, os.path.getsize(out), 'bytes')

# 生成 image_map.js (name -> images/xxx.jpg)
with open(os.path.join(PROJ, 'image_map.js'), 'w', encoding='utf-8') as f:
    f.write("// 动物图片映射 - 自动生成\nconst ANIMAL_IMAGE_MAP = {\n")
    for a in all_animals:
        f.write(f'  "{a["name"]}": "{a["image"]}",\n')
    f.write("};\n")
print('已写入 image_map.js')

# 校验
with open(out, 'r', encoding='utf-8') as f:
    check = json.load(f)
print('校验OK:', check['totalAnimals'], '条,字段:', list(check['animals'][0].keys()))
