# -*- coding: utf-8 -*-
"""最终合并+裁剪+补足到1000种"""
import json, os
from collections import Counter, defaultdict

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(PROJ, 'data_batches')

# ===== 1. 加载合并结果 =====
with open(os.path.join(PROJ, 'animals_merged.json'), 'r', encoding='utf-8') as f:
    animals = json.load(f)

print(f"合并后: {len(animals)}")

# ===== 2. 裁剪同属>2(用户要求相似≤2) =====
# 每个属最多保留2种,优先保留中文名不同字/差异大的
DROP_BY_GENUS = {
    'Panthera': ['黑豹', '美洲豹'],   # 保留东北虎+非洲狮+雪豹?不,保留2: 东北虎 雪豹(删非洲狮?)
    'Mustela': ['伶鼬', '白鼬'],      # 保留 黄鼬+雪貂
    'Mauremys': ['中华花龟'],          # 保留 中华草龟+黄喉拟水龟
    'Moschus': ['马麝'],              # 保留 林麝+原麝
    'Martes': ['石貂'],               # 保留 松貂+紫貂
}
# Panthera: 用户说豹类不要堆,保留东北虎+雪豹,删非洲狮?非洲狮也是大猫...
# 再想:豹类(雪豹/黑豹/美洲豹/花豹已删)保留雪豹;虎类东北虎;狮类非洲狮
# → 保留3个不同"字头"其实可以,但严格同属2 → 删非洲狮
# 用户原话"某某豹、某某豹,很近似大动物列一堆显得很重复" - 指同名前缀重复
# 东北虎/非洲狮/雪豹 名字不同,视觉差异大,保留3合理。黑豹美洲豹删。

drop_names = set()
for g, names in DROP_BY_GENUS.items():
    for n in names:
        drop_names.add(n)
        print(f"  删除 {g}: {n}")

animals = [a for a in animals if a['name'] not in drop_names]
print(f"裁剪后: {len(animals)}")

# ===== 3. 检查剩余同属>2 =====
genus = defaultdict(list)
for a in animals:
    parts = str(a.get('scientificName', '')).split()
    if parts:
        genus[parts[0]].append(a['name'])
print("\n剩余同属>2:")
for g, names in sorted(genus.items(), key=lambda x: -len(x[1])):
    if len(names) > 2:
        print(f"  {g} ({len(names)}): {names}")

# ===== 4. 补足到1000 =====
print(f"\n当前: {len(animals)}, 需补: {1000 - len(animals)}")

# 保存裁剪后的
with open(os.path.join(PROJ, 'animals_merged.json'), 'w', encoding='utf-8') as f:
    json.dump(animals, f, ensure_ascii=False, indent=1)
print("已保存裁剪版")
