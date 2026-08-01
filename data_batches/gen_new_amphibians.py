# -*- coding: utf-8 -*-
"""Generate 30 new amphibian species (两栖类) - no duplicates with existing 19 species,
max 2 per genus, real scientific names."""
import json, os, re

OUT = r"C:/Users/Administrator/Desktop/animal-world-mini-program/data_batches/new_amphibians.json"

def sp(name, en, sci, habitat, diet, size, weight, length_m, status, emoji, desc, img):
    return {
        "name": name,
        "englishName": en,
        "scientificName": sci,
        "category": "两栖类",
        "habitat": habitat,
        "diet": diet,
        "size": size,
        "weight": weight,
        "length": length_m,
        "status": status,
        "emoji": emoji,
        "description": desc,
        "imagePrompt": img,
    }

def img(en, sci, detail):
    return ("A photorealistic wildlife photograph of a %s (%s), %s, National Geographic style." % (en, sci, detail))

D = []

# ---------- 蛙类 Frogs (Anura) ----------
D.append(sp("泽蛙", "Rice-paddy Frog", "Fejervarya limnocharis",
    "中国南方及东南亚的稻田、池塘与沼泽", "昆虫、蜘蛛、蚯蚓等小型无脊椎动物",
    "体长5-7厘米", "10-20克", 0.05, "无危(LC)", "🐸",
    "常见于稻田与池塘的褐色小蛙,背部有数条纵行肤棱,雄蛙鸣囊发达,雨季叫声响彻田野,是农田生态中数量最多的蛙类之一。",
    img("Rice-paddy Frog", "Fejervarya limnocharis", "small brown frog with longitudinal skin ridges on its back, sitting on a muddy rice paddy edge among green rice seedlings, dew drops on skin, soft morning light")))

D.append(sp("金线侧褶蛙", "Golden-lined Pond Frog", "Pelophylax plancyi",
    "中国东部平原的水田、湖泊与河沟", "昆虫、虾、小鱼及水生无脊椎动物",
    "体长5-9厘米", "20-50克", 0.06, "近危(NT)", "🐸",
    "背侧褶金黄醒目,体型匀称,生活于平原水田与湖泊,跳跃敏捷,以昆虫为食,是长江中下游常见的绿色蛙类。",
    img("Golden-lined Pond Frog", "Pelophylax plancyi", "green frog with bright golden dorsolateral folds, basking on a lotus leaf at the edge of a calm pond, golden sunlight reflection")))

D.append(sp("双团棘胸蛙", "Boulenger's Spiny Frog", "Quasipaa boulengeri",
    "中国南方及越南北部的山区溪流与石缝", "昆虫、小鱼、虾蟹及蠕虫",
    "体长8-12厘米", "150-400克", 0.11, "易危(VU)", "🐸",
    "雄蛙胸部有两团黑色角质刺棘,体型粗壮,栖息于山溪石缝,昼伏夜出,捕食昆虫与小鱼,因肉质鲜美曾遭过度捕猎。",
    img("Boulenger's Spiny Frog", "Quasipaa boulengeri", "large robust brown frog with two black spiny patches on the male's chest, perched on wet rocks beside a fast mountain stream")))

D.append(sp("太平洋雨蛙", "Pacific Tree Frog", "Pseudacris regilla",
    "北美西部林地、草地与湿地,从海平面到高山", "昆虫、蜘蛛等小型节肢动物",
    "体长3-5厘米", "3-8克", 0.045, "无危(LC)", "🐸",
    "北美西部常见的绿色小树蛙,眼后有一条深色条纹,趾端膨大善攀爬,雨后十分活跃,鸣声清脆,适应力极强。",
    img("Pacific Tree Frog", "Pseudacris regilla", "small bright green tree frog with a dark stripe through the eye, clinging to a fern leaf in a damp Pacific Northwest forest, dew droplets")))

D.append(sp("灰雨蛙", "Gray Tree Frog", "Hyla versicolor",
    "北美东部的落叶林、池塘边树木与灌丛", "昆虫、飞蛾、蟋蟀等",
    "体长4-6厘米", "5-12克", 0.05, "无危(LC)", "🐸",
    "体色灰绿多变,能随环境缓慢变色,背上有不规则深色斑,栖息于林间树木,叫声似悠长颤音,是北美常见树蛙。",
    img("Gray Tree Frog", "Hyla versicolor", "gray-green tree frog with irregular dark blotches sitting on a mossy tree branch, camouflage against lichen-covered bark, soft forest light")))

D.append(sp("大树蛙", "Dennys' Tree Frog", "Zhangixalus dennysi",
    "中国南方及东南亚的亚热带常绿阔叶林", "昆虫、蜘蛛及其他小型无脊椎动物",
    "体长6-10厘米", "30-60克", 0.08, "无危(LC)", "🐸",
    "中国南方的大型树蛙,背部绿色带棕色斑纹,指间蹼发达可滑翔,常栖息于高大乔木,繁殖期集群到水塘求偶产卵。",
    img("Dennys' Tree Frog", "Zhangixalus dennysi", "large vivid green tree frog with brown markings and wide webbed feet, perched on a broad rainforest leaf high in a tree canopy")))

D.append(sp("黑蹼树蛙", "Black-webbed Tree Frog", "Rhacophorus kio",
    "东南亚及中国南方的热带雨林树冠层", "飞行昆虫、蜘蛛等",
    "体长7-9厘米", "20-40克", 0.08, "无危(LC)", "🐸",
    "趾间黑色蹼膜宽大如翼,能从树冠滑翔数米,背部绿色腹面橙黄,栖息于东南亚雨林,是著名的飞蛙。",
    img("Black-webbed Tree Frog", "Rhacophorus kio", "green tree frog with wide black webbing between toes spread like gliding wings, vivid orange underside, mid-leap over a tropical rainforest stream")))

D.append(sp("东方铃蟾", "Oriental Fire-bellied Toad", "Bombina orientalis",
    "中国东北、华北及朝鲜半岛的山溪石下与浅水坑", "昆虫、蠕虫及水生小动物",
    "体长3-5厘米", "5-15克", 0.045, "无危(LC)", "🐸",
    "腹面橙红与蓝黑交织,受惊时翻背露出警戒色,四肢上举装死,栖息于山溪石下,是我国北方珍稀的铃蟾。",
    img("Oriental Fire-bellied Toad", "Bombina orientalis", "small warty toad with bright orange and blue-black mottled belly, floating at the water surface of a rocky mountain pool, unken reflex posture")))

D.append(sp("欧洲黄腹铃蟾", "Yellow-bellied Toad", "Bombina variegata",
    "中欧与南欧的山地浅水塘、泥沼与石坑", "水生昆虫、蠕虫等小型无脊椎动物",
    "体长4-6厘米", "5-15克", 0.05, "无危(LC)", "🐸",
    "腹面柠檬黄带黑色斑纹,受威胁时四肢朝天展示警示色,昼伏夜出,栖息于欧洲浅水塘与泥沼,叫声轻柔。",
    img("Yellow-bellied Toad", "Bombina variegata", "small toad with lemon-yellow belly patterned with dark blotches, resting on a sun-warmed stone by a shallow European woodland pond")))

D.append(sp("东部锄足蟾", "Eastern Spadefoot Toad", "Scaphiopus holbrookii",
    "北美东部沙质土壤的林地与农田边缘", "昆虫、蜘蛛、蚯蚓等",
    "体长5-7厘米", "30-60克", 0.065, "无危(LC)", "🐸",
    "后足有坚硬的角质锄突,善掘土打洞,暴风雨后大量出现繁殖,叫声尖锐刺耳,是北美东部夜行性的穴居蟾蜍。",
    img("Eastern Spadefoot Toad", "Scaphiopus holbrookii", "plump brown toad with vertical cat-like pupils and a dark spade-shaped tubercle on each hind foot, half-buried in sandy soil")))

D.append(sp("加州锄足蟾", "California Spadefoot Toad", "Spea hammondii",
    "美国加州干旱的草地与林地,雨季积水洼地", "昆虫、蜘蛛及其他节肢动物",
    "体长4-6厘米", "25-50克", 0.06, "无危(LC)", "🐸",
    "栖息于加州干旱地带,靠后足角状锄突掘洞躲藏,雨季降雨后短暂出现繁殖,能分泌刺鼻气味抵御天敌。",
    img("California Spadefoot Toad", "Spea hammondii", "smooth-skinned toad with prominent golden eyes and vertical pupils emerging from a burrow in cracked dry Californian grassland soil")))

D.append(sp("北美窄口蟾", "Eastern Narrow-mouthed Toad", "Gastrophryne carolinensis",
    "北美东南部潮湿林地、草地与城市花园", "白蚁、蚂蚁等小型昆虫",
    "体长2-3厘米", "3-8克", 0.03, "无危(LC)", "🐸",
    "体小呈卵圆形,吻尖如铲,善掘土,以白蚁和蚂蚁为食,叫声似羊羔咩咩,是北美东南部的奇特小蟾蜍。",
    img("Eastern Narrow-mouthed Toad", "Gastrophryne carolinensis", "tiny oval-shaped brown frog with a pointed snout, sitting on a rotting log beside a termite trail in a damp southern forest")))

D.append(sp("花狭口蛙", "Asian Painted Frog", "Kaloula pulchra",
    "东南亚及中国华南的农田、林缘与居民区", "蚂蚁、白蚁及其他小型昆虫",
    "体长6-8厘米", "40-80克", 0.07, "无危(LC)", "🐸",
    "体色棕黄带黑色条纹,形似被挤压的圆球,雨后大量出现,叫声洪亮如牛,常见于东南亚与华南的庭园池塘边。",
    img("Asian Painted Frog", "Kaloula pulchra", "plump round frog with brown body and dark stripes, sitting on wet concrete near a puddle after rain in a tropical garden, inflated vocal sac")))

D.append(sp("中华髭蟾", "Emei Moustache Toad", "Leptobrachium boringii",
    "中国四川峨眉山等地的清澈山溪", "昆虫、蠕虫、小鱼等",
    "体长7-9厘米", "50-100克", 0.08, "易危(VU)", "🐸",
    "峨眉山著名珍稀蛙类,雄蛙上唇长有黑色角质刺,形如胡须,栖息于清澈山溪,繁殖期叫声低沉如牛鸣。",
    img("Emei Moustache Toad", "Leptobrachium boringii", "dark gray-brown toad with black horny nuptial spines on the upper lip like a moustache, resting on a wet rock in a clear mountain stream")))

D.append(sp("峨眉角蟾", "Emei Horned Toad", "Megophrys omeimontis",
    "中国四川峨眉山及邻近山区的潮湿林下", "昆虫、蜘蛛等小型节肢动物",
    "体长5-7厘米", "20-40克", 0.06, "无危(LC)", "🐸",
    "眼上方有短角状突起,体色似枯叶利于伪装,栖息于峨眉山潮湿林下落叶层,昼伏夜出捕食昆虫。",
    img("Emei Horned Toad", "Megophrys omeimontis", "camouflaged brown toad with short horn-like projections above the eyes, blending perfectly into a bed of dead leaves on a humid forest floor")))

D.append(sp("产婆蟾", "Midwife Toad", "Alytes obstetricans",
    "西欧与中欧的石堆、洞穴及潮湿林地", "昆虫、蠕虫等小型无脊椎动物",
    "体长4-5厘米", "5-15克", 0.05, "无危(LC)", "🐸",
    "欧洲奇蛙,雄蛙将卵带缠绕在后腿上携带孵化,护卵如产婆,体灰褐多疣,夜行性,栖息于石堆与洞穴。",
    img("Midwife Toad", "Alytes obstetricans", "warty gray-brown toad with a string of eggs wrapped around its hind legs, hopping over mossy stones in a twilight European woodland")))

D.append(sp("弹琴蛙", "Music Frog", "Nidirana adenopleura",
    "中国南方及东南亚的山地静水池塘与沼泽", "昆虫、水生小动物",
    "体长4-5厘米", "10-25克", 0.045, "无危(LC)", "🐸",
    "鸣声清脆悦耳如弹琴,栖息于高山静水池塘,常筑泥巢保护卵群,分布于中国南方与东南亚山地。",
    img("Music Frog", "Nidirana adenopleura", "slender brown-green frog calling near a still mountain pond, inflated vocal sac, surrounded by water plants and soft morning mist")))

D.append(sp("澳洲绿树蛙", "Australian Green Tree Frog", "Litoria caerulea",
    "澳大利亚东部及新几内亚的森林、湿地与城镇", "昆虫、蜘蛛、小型脊椎动物",
    "体长8-12厘米", "50-150克", 0.10, "无危(LC)", "🐸",
    "体色翠绿带白色斑点,趾垫发达善攀爬,性情温顺常栖于人类居所附近,是澳大利亚最著名的树蛙。",
    img("Australian Green Tree Frog", "Litoria caerulea", "large bright green tree frog with white spots and big golden eyes, clinging to a eucalyptus branch, glossy skin, warm Australian sunlight")))

# ---------- 蝾螈类 Salamanders (Caudata) ----------
D.append(sp("红瘰疣螈", "Red-knobbed Newt", "Tylototriton shanjing",
    "中国云南及东南亚山地的林间静水塘", "水生昆虫、蚯蚓、小鱼虾",
    "体长13-20厘米", "30-60克", 0.18, "近危(NT)", "🦎",
    "体侧有成排红色疣粒,形如红珠串,黑色身体配橙红斑纹,栖息于云南山地林间,是我国珍稀的螈类。",
    img("Red-knobbed Newt", "Tylototriton shanjing", "black newt with a row of bright orange-red knobs along each side and orange head ridges, resting on wet moss beside a mountain pool in Yunnan")))

D.append(sp("贵州疣螈", "Guizhou Newt", "Tylototriton kweichowensis",
    "中国贵州高原的山间静水塘与湿地", "水生昆虫、蠕虫及小型无脊椎动物",
    "体长12-16厘米", "15-30克", 0.14, "易危(VU)", "🦎",
    "贵州特有珍稀蝾螈,体背棕黑,头背有脊棱,皮肤布满疣粒,栖息于山间静水塘,以水生昆虫为食。",
    img("Guizhou Newt", "Tylototriton kweichowensis", "dark brown newt with prominent cranial ridges and warty skin, swimming slowly in a clear highland pond surrounded by grassy wetland")))

D.append(sp("红背无肺螈", "Eastern Red-backed Salamander", "Plethodon cinereus",
    "北美东部潮湿的落叶林、石下与朽木中", "螨虫、蚂蚁、甲虫等小型无脊椎动物",
    "体长8-12厘米", "3-6克", 0.10, "无危(LC)", "🦎",
    "北美常见的小型无肺螈,背部红色或灰色条纹,没有肺完全靠皮肤呼吸,栖息于落叶层与朽木之下。",
    img("Eastern Red-backed Salamander", "Plethodon cinereus", "small slender salamander with a bright red stripe down its back, gliding over damp forest leaf litter and moss, macro detail")))

D.append(sp("斑泥螈", "Common Mudpuppy", "Necturus maculosus",
    "北美东部与中部的湖泊、河流与水库", "小鱼、虾、蠕虫及水生昆虫",
    "体长20-33厘米", "100-300克", 0.30, "无危(LC)", "🦎",
    "终生保留鲜红色外鳃的水生蝾螈,体灰褐带深色斑点,四肢短壮,夜行捕食小鱼虾,见于北美湖泊河流。",
    img("Common Mudpuppy", "Necturus maculosus", "aquatic salamander with bushy red external gills and dark spots on a gray-brown body, resting on the muddy bottom of a clear lake")))

D.append(sp("洞螈", "Olm", "Proteus anguinus",
    "斯洛文尼亚及巴尔干半岛的喀斯特洞穴地下水", "洞穴虾、蠕虫等小型水生动物",
    "体长20-30厘米", "15-30克", 0.30, "易危(VU)", "🦎",
    "生活在黑暗洞穴中的白色盲螈,终身保留外鳃,皮肤苍白半透明,可数十年不进食,是斯洛文尼亚的国宝。",
    img("Olm", "Proteus anguinus", "pale white blind cave salamander with feathery pink external gills, translucent skin showing internal organs, swimming in dark karst cave water, eerie blue glow")))

D.append(sp("陆巨螈", "Pacific Giant Salamander", "Dicamptodon tenebrosus",
    "北美太平洋沿岸的湿润森林与山溪", "昆虫、蚯蚓、小鱼及小型两栖动物",
    "体长25-35厘米", "200-500克", 0.33, "无危(LC)", "🦎",
    "北美最大的陆生蝾螈,体棕褐色带云状斑纹,性情凶猛会咬人,栖息于太平洋沿岸湿润森林的溪流边。",
    img("Pacific Giant Salamander", "Dicamptodon tenebrosus", "large stout brown salamander with dark marbled blotches, sitting on wet rocks beside a cascading Pacific Northwest stream, misty forest background")))

D.append(sp("中国小鲵", "Chinese Salamander", "Hynobius chinensis",
    "中国长江中下游山区的清澈溪流", "水生昆虫、蠕虫及小型甲壳动物",
    "体长10-15厘米", "20-50克", 0.13, "易危(VU)", "🦎",
    "我国特有的古老小鲵,体长仅十余厘米,栖息于高山溪流,繁殖期上岸产卵,是研究两栖类进化的活化石。",
    img("Chinese Salamander", "Hynobius chinensis", "small dark brown salamander with a long tail, gliding over smooth stones in a shallow clear mountain stream in China, cool blue water")))

D.append(sp("三趾两栖螈", "Three-toed Amphiuma", "Amphiuma tridactylum",
    "美国东南部的沼泽、沟渠与缓流水域", "鱼、蛙、小龙虾及水生昆虫",
    "体长50-100厘米", "300-1000克", 0.75, "无危(LC)", "🦎",
    "身体细长如鳗,前后足仅有三趾,栖息于美国东南部沼泽,夜行性,以鱼类与甲壳类为食,性情凶猛。",
    img("Three-toed Amphiuma", "Amphiuma tridactylum", "eel-like dark gray aquatic salamander with tiny three-toed limbs, coiled in murky swamp water among water hyacinths, southern US bayou")))

D.append(sp("大泥螈", "Greater Siren", "Siren lacertina",
    "美国东南部的湖泊、沼泽与缓慢河流", "水生昆虫、蠕虫、小鱼及蝌蚪",
    "体长40-90厘米", "200-800克", 0.60, "无危(LC)", "🦎",
    "体形似鳗,终生保留外鳃,仅有前肢没有后肢,栖息于北美东南部水域,是现存最大的泥螈类动物。",
    img("Greater Siren", "Siren lacertina", "long eel-like aquatic salamander with feathery external gills and only front legs, gliding through dark tannin-stained swamp water, surface ripples")))

# ---------- 蚓螈类 Caecilians (Gymnophiona) ----------
D.append(sp("墨西哥蚓螈", "Mexican Burrowing Caecilian", "Dermophis mexicanus",
    "墨西哥及中美洲的潮湿土壤与落叶层", "蚯蚓、白蚁、昆虫幼虫等",
    "体长25-40厘米", "50-150克", 0.35, "无危(LC)", "🪱",
    "外形似蚯蚓的无足两栖动物,体表有环状褶皱,栖息于墨西哥潮湿土壤中,靠嗅觉与触觉捕食蠕虫。",
    img("Mexican Burrowing Caecilian", "Dermophis mexicanus", "legless worm-like amphibian with segmented ringed skin and tiny eyes, burrowing through dark moist tropical soil, shiny dark purple body")))

D.append(sp("环纹蚓螈", "Ringed Caecilian", "Siphonops annulatus",
    "南美洲雨林的地下与潮湿腐殖层", "蚯蚓、昆虫幼虫等土壤无脊椎动物",
    "体长30-45厘米", "50-200克", 0.40, "无危(LC)", "🪱",
    "体表布满环形皱褶,形似大蚯蚓,生活于南美雨林地下,以蚯蚓和昆虫幼虫为食,视力退化但嗅觉灵敏。",
    img("Ringed Caecilian", "Siphonops annulatus", "blue-gray legless amphibian with distinct ring-like body segments, half-emerged from rainforest soil, glistening moist skin, macro shot")))

D.append(sp("版纳鱼螈", "Banna Caecilian", "Ichthyophis bannanicus",
    "中国云南西双版纳的溪流软泥与湿地", "水生昆虫、蠕虫及小型无脊椎动物",
    "体长25-40厘米", "40-100克", 0.35, "易危(VU)", "🪱",
    "我国唯一的蚓螈类动物,体细长如蛇,栖息于西双版纳溪流软泥中,以水生无脊椎动物为食,野外极为罕见。",
    img("Banna Caecilian", "Ichthyophis bannanicus", "elongated dark purplish legless amphibian with faint yellow lateral stripes, gliding through soft mud at the edge of a tropical stream in Xishuangbanna, China")))

# ---------- validation ----------
assert len(D) == 30, "need exactly 30, got %d" % len(D)

# existing species check (from animals_data.json)
with open(r"C:/Users/Administrator/Desktop/animal-world-mini-program/animals_data.json", encoding="utf-8") as f:
    existing = json.load(f)["animals"]
existing_names = {a.get("name") for a in existing}
existing_scis = {a.get("scientificName").lower() for a in existing}
new_names = [d["name"] for d in D]
new_scis = [d["scientificName"].lower() for d in D]

dups_existing = [n for n in new_names if n in existing_names] + [s for s in new_scis if s in existing_scis]
assert not dups_existing, "dup with existing: %s" % dups_existing
assert len(set(new_scis)) == 30, "dup scientific names within batch"
assert len(set(new_names)) == 30, "dup names within batch"

# genus limit: max 2 per genus (including existing species' genera)
def genus(sci):
    return sci.split()[0].lower()
from collections import Counter
g = Counter(genus(s) for s in new_scis)
g_existing = Counter(genus(a["scientificName"]) for a in existing if a.get("scientificName"))
bad = {k: v + g_existing[k] for k, v in g.items() if v + g_existing.get(k, 0) > 2}
assert not bad, "genus over limit: %s" % bad

# description length 40-80
for d in D:
    L = len(d["description"])
    assert 40 <= L <= 80, "%s desc len %d" % (d["name"], L)
    assert d["imagePrompt"].startswith("A photorealistic wildlife photograph of a ")
    assert d["imagePrompt"].rstrip().endswith("National Geographic style.")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(D, f, ensure_ascii=False, indent=1)

print("OK: wrote %d entries to %s" % (len(D), OUT))
print("Families:", sorted(set(d["scientificName"].split()[0].lower() for d in D)))
