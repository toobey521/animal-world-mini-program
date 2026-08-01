# -*- coding: utf-8 -*-
"""Generate 40 new insect species -> new_insects3.json (batch 3)."""
import json, os

BASE = r"C:/Users/Administrator/Desktop/animal-world-mini-program"
OUT = os.path.join(BASE, "data_batches", "new_insects3.json")

def E(name, en, sc, habitat, diet, size, weight, length, status, emoji, desc, img):
    return {
        "name": name, "englishName": en, "scientificName": sc, "category": "昆虫类",
        "habitat": habitat, "diet": diet, "size": size, "weight": weight,
        "length": length, "status": status, "emoji": emoji,
        "description": desc, "imagePrompt": img,
    }

data = [
# ---------- 螳螂目 Mantodea (4) ----------
E("幽灵螳螂", "Ghost Mantis", "Phyllocrania paradoxa",
  "非洲干旱林地与灌木丛", "捕食果蝇、飞蛾等小飞虫",
  "体长约5厘米", "1-2克", 0.05, "未评估(NE)", "🦗",
  "体表布满枯叶般的皱褶与干枯纹理,头冠形似残破叶尖,常倒挂枝头随风轻摆,与枯叶融为一体,是非洲最著名的拟态螳螂之一。",
  "A photorealistic macro photograph of a Ghost Mantis (Phyllocrania paradoxa), brown leaf-mimicking mantis with a curled head crest and withered-leaf texture, hanging upside down on a dry twig, National Geographic style."),
E("刺花螳螂", "Spiny Flower Mantis", "Pseudocreobotra wahlbergii",
  "非洲东部与南部草原灌丛", "捕食蜜蜂、蝴蝶等访花昆虫",
  "体长约4厘米", "1-2克", 0.04, "未评估(NE)", "🦗",
  "通体布满锐利尖刺,腹部后翘,体色翠绿带彩色花纹,宛如一朵带刺的小花,以伏击采蜜昆虫为生,是非洲草原上的奇特猎手。",
  "A photorealistic macro photograph of a Spiny Flower Mantis (Pseudocreobotra wahlbergii), green mantis covered with sharp spines and colorful flower-like markings, perched on a blossom, National Geographic style."),
E("小提琴螳螂", "Wandering Violin Mantis", "Gongylus gongylodes",
  "印度与斯里兰卡干旱林地", "捕食小型飞虫",
  "体长约8厘米", "2-3克", 0.08, "未评估(NE)", "🦗",
  "头胸细长如小提琴琴颈,前足胫节生有宽阔叶状扩展,体色枯黄,静立枝头如一片枯叶,是形态最为奇特的螳螂之一。",
  "A photorealistic macro photograph of a Wandering Violin Mantis (Gongylus gongylodes), slender mantis with a violin-shaped head and thorax and wide leaf-like front legs, on a dry branch, National Geographic style."),
E("眼斑螳螂", "Giant African Stick Mantis", "Heterochaeta orientalis",
  "非洲热带稀树草原", "捕食飞蛾、蝗虫等昆虫",
  "体长约15厘米", "4-6克", 0.15, "未评估(NE)", "🦗",
  "非洲体型最长的螳螂之一,头呈三角形,复眼巨大如猫眼,胸腹细长如枝条,善于伏击飞过的昆虫,是草原上的顶级伪装猎手。",
  "A photorealistic macro photograph of a Giant African Stick Mantis (Heterochaeta orientalis), extremely elongated brown mantis with a triangular head and large cat-like compound eyes, on a savanna grass stem, National Geographic style."),
# ---------- 鳞翅目 蝴蝶 (9) ----------
E("猫头鹰蝶", "Forest Giant Owl Butterfly", "Caligo eurilochus",
  "中南美洲热带雨林", "幼虫取食芭蕉科植物,成虫吸食腐果汁液",
  "翅展约16厘米", "3-5克", 0.16, "无危(LC)", "🦋",
  "翅腹面生有酷似猫头鹰双眼的巨大眼斑,可惊吓捕食者,翅展可达16厘米,是南美体型最大的蝴蝶之一,黄昏时在林间悠然飞行。",
  "A photorealistic macro photograph of a Forest Giant Owl Butterfly (Caligo eurilochus), large brown butterfly with huge owl-eye spots on the underwings, resting on a rainforest trunk, National Geographic style."),
E("地图蝶", "Map Butterfly", "Araschnia levana",
  "欧洲温带林缘与草甸", "幼虫取食荨麻,成虫吸食花蜜",
  "翅展约4厘米", "0.2-0.4克", 0.04, "无危(LC)", "🦋",
  "翅面斑纹形似地图上的河流与海岸线,故得此名,春型橙红、夏型黑白,季节差异显著,是研究昆虫季节多型现象的经典物种。",
  "A photorealistic macro photograph of a Map Butterfly (Araschnia levana), orange and dark butterfly with map-like vein patterns on the wings, resting on a meadow flower, National Geographic style."),
E("88蝶", "88 Butterfly", "Diaethria clymena",
  "中美洲热带林缘与溪谷", "幼虫取食苋科植物,成虫吸食腐果与汁液",
  "翅展约4厘米", "0.2-0.4克", 0.04, "无危(LC)", "🦋",
  "后翅腹面生有清晰醒目的数字88斑纹,因此得名,翅背黑色缀蓝绿条纹,飞行迅速,常见于中美洲林间溪畔,辨识度极高。",
  "A photorealistic macro photograph of a 88 Butterfly (Diaethria clymena), black butterfly with blue-green wing bands and clear number 88 markings on the underwings, on a tropical leaf, National Geographic style."),
E("玻璃翼蝶", "Glasswing Butterfly", "Greta oto",
  "中美洲雨林林荫溪畔", "幼虫取食茄科植物,成虫吸食花蜜",
  "翅展约6厘米", "0.2-0.5克", 0.06, "无危(LC)", "🦋",
  "双翅透明如玻璃,仅翅脉与边缘清晰可见,飞行时几近隐形,是中美洲雨林的奇迹,也是科普展览中最受欢迎的蝴蝶之一。",
  "A photorealistic macro photograph of a Glasswing Butterfly (Greta oto), butterfly with completely transparent wings and dark veins, perched on a rainforest leaf with soft backlight, National Geographic style."),
E("亚历山大鸟翼蝶", "Queen Alexandra's Birdwing", "Ornithoptera alexandrae",
  "巴布亚新几内亚北部低地雨林", "幼虫取食马兜铃科藤蔓,成虫吸食花蜜",
  "翅展可达28厘米", "5-8克", 0.28, "濒危(EN)", "🦋",
  "全球最大的蝴蝶,雌虫翅展可达28厘米,翅面褐白相间,仅分布于巴布亚新几内亚雨林,因栖息地破坏而濒危,极为珍贵。",
  "A photorealistic macro photograph of a Queen Alexandra's Birdwing (Ornithoptera alexandrae), the world's largest butterfly with brown and cream wings, female, in a lowland rainforest clearing, National Geographic style."),
E("歌利亚鸟翼蝶", "Goliath Birdwing", "Ornithoptera goliath",
  "新几内亚岛低地雨林", "幼虫取食马兜铃科植物,成虫吸食花蜜",
  "翅展可达22厘米", "4-6克", 0.22, "未评估(NE)", "🦋",
  "全球第二大蝴蝶,雄虫翅面金黄与翠绿交织,黑色斑纹如丝绒,飞行强劲,栖息于新几内亚雨林树冠层,是鸟翼蝶中的巨无霸。",
  "A photorealistic macro photograph of a Goliath Birdwing (Ornithoptera goliath), huge butterfly with golden-yellow and green wings with black markings, male, flying over a tropical canopy, National Geographic style."),
E("红颈鸟翼蝶", "Rajah Brooke's Birdwing", "Trogonoptera brookiana",
  "东南亚热带雨林溪谷", "幼虫取食马兜铃科植物,成虫吸食花蜜",
  "翅展约17厘米", "3-5克", 0.17, "未评估(NE)", "🦋",
  "雄虫翅面墨绿泛金属光泽,颈部生有一圈鲜红绒毛,黑红绿三色对比强烈,被誉为马来西亚最美丽的蝴蝶,是婆罗洲雨林的明星蝶种。",
  "A photorealistic macro photograph of a Rajah Brooke's Birdwing (Trogonoptera brookiana), black-green butterfly with red collar bristles and metallic green wing patches, male, at a rainforest stream, National Geographic style."),
E("大紫蛱蝶", "Great Purple Emperor", "Sasakia charonda",
  "东亚山地阔叶林", "幼虫取食朴树叶片,成虫吸食树液与腐果",
  "翅展约11厘米", "1-2克", 0.11, "未评估(NE)", "🦋",
  "日本国蝶,雄蝶翅面泛蓝紫色金属光泽,点缀白色斑纹,飞行优雅从容,栖息于山间溪谷林带,是东亚最具代表性的珍稀蛱蝶。",
  "A photorealistic macro photograph of a Great Purple Emperor (Sasakia charonda), large butterfly with iridescent purple-blue wings and white spots, male, on a tree trunk in a mountain forest, National Geographic style."),
E("尤利西斯蝶", "Ulysses Butterfly", "Papilio ulysses",
  "澳大利亚东北部与巴布亚新几内亚雨林", "幼虫取食芸香科植物,成虫吸食花蜜",
  "翅展约12厘米", "2-3克", 0.12, "无危(LC)", "🦋",
  "翅面呈深邃的电光蓝色,镶黑色外缘,飞行时如蓝色闪电划过雨林,是澳大利亚的国蝶之一,被当地人视为幸运的象征。",
  "A photorealistic macro photograph of a Ulysses Butterfly (Papilio ulysses), brilliant electric-blue butterfly with black wing borders and swallowtails, on a rainforest blossom, National Geographic style."),
# ---------- 鳞翅目 蛾 (5) ----------
E("月亮蛾", "Comet Moth", "Argema mittrei",
  "马达加斯加热带雨林", "幼虫取食多种树木叶片,成虫口器退化不进食",
  "翅展约20厘米(含尾突)", "2-4克", 0.2, "未评估(NE)", "🦋",
  "马达加斯加特有的大型天蚕蛾,前翅黄绿色,后翅拖着一对飘逸长尾,斑纹如月华洒落,被誉为世界上最美的蛾类之一。",
  "A photorealistic macro photograph of a Comet Moth (Argema mittrei), yellow-green moth with long elegant tail streamers on the hindwings and crescent markings, resting in a Madagascan rainforest, National Geographic style."),
E("孔雀蛾", "Giant Peacock Moth", "Saturnia pyri",
  "欧洲南部果园与林地", "幼虫取食果树与榆树叶片,成虫不进食",
  "翅展约15厘米", "2-4克", 0.15, "无危(LC)", "🦋",
  "欧洲体型最大的蛾类,翅面灰褐色,四翅各饰一枚孔雀翎般的大眼斑,夜间飞行,春季在果园林间飞舞,如夜色中的精灵。",
  "A photorealistic macro photograph of a Giant Peacock Moth (Saturnia pyri), large grey-brown moth with four huge peacock-eye spots, resting on an orchard tree bark, National Geographic style."),
E("帝王蛾", "Imperial Moth", "Eacles imperialis",
  "北美东部落叶阔叶林", "幼虫取食多种阔叶树叶片,成虫不进食",
  "翅展约15厘米", "2-4克", 0.15, "无危(LC)", "🦋",
  "北美大型天蚕蛾,翅面明黄底色缀以紫褐色斑纹,形态华丽如帝袍,幼虫体型粗壮,成虫口器退化,仅靠体内养分存活约一周。",
  "A photorealistic macro photograph of an Imperial Moth (Eacles imperialis), large yellow moth with purple-brown blotches and wing patterns, resting on oak leaves in a North American forest, National Geographic style."),
E("大力神蛾", "Hercules Moth", "Coscinocera hercules",
  "澳大利亚与新几内亚雨林", "幼虫取食多种树木叶片,成虫不进食",
  "翅展可达27厘米", "5-8克", 0.27, "未评估(NE)", "🦋",
  "世界上翅面积最大的蛾类,翅展可达27厘米,翅面黄褐交织,后翅拖有修长尾突,斑纹如蛇头般诡异,是南半球雨林的巨型飞蛾。",
  "A photorealistic macro photograph of a Hercules Moth (Coscinocera hercules), huge brown-yellow moth with long hindwing tails and snake-head markings, the largest moth by wing area, on a rainforest leaf, National Geographic style."),
E("红尾大蚕蛾", "Chinese Moon Moth", "Actias dubernardi",
  "中国西南山地森林", "幼虫取食松科与壳斗科植物叶片,成虫不进食",
  "翅展约12厘米(含尾突)", "1-3克", 0.12, "未评估(NE)", "🦋",
  "中国特有的美丽天蚕蛾,雌雄异色,雄蛾翅面嫩绿、后翅拖粉红长尾,如飘带飞舞,观赏价值极高,深受蝴蝶收藏家喜爱。",
  "A photorealistic macro photograph of a Chinese Moon Moth (Actias dubernardi), male moth with pale green wings and long pink tail streamers, perched on a twig in a misty mountain forest, National Geographic style."),
# ---------- 鞘翅目 金龟/兜虫 (4) ----------
E("南洋大兜虫", "Atlas Beetle", "Chalcosoma atlas",
  "东南亚热带雨林", "幼虫腐食朽木,成虫吸食树液与腐果",
  "体长约12厘米(含角)", "15-30克", 0.12, "无危(LC)", "🪲",
  "东南亚体型最大的兜虫之一,雄虫头胸部各生三根弯角,体色乌黑泛金属光泽,外形如科幻巨兽,是甲虫收藏界的经典宠儿。",
  "A photorealistic macro photograph of an Atlas Beetle (Chalcosoma atlas), huge black beetle with three long horns on the head and thorax, glossy metallic body, on a rainforest log, National Geographic style."),
E("象兜虫", "Elephant Beetle", "Megasoma elephas",
  "中美洲低地雨林", "幼虫腐食朽木,成虫吸食树液与腐果",
  "体长约13厘米(含角)", "20-35克", 0.13, "无危(LC)", "🪲",
  "雄虫头部生有粗壮的象鼻状犄角,体表覆金黄色细毛,体态魁梧,体重在甲虫中名列前茅,栖息于中美洲雨林,以树液为食。",
  "A photorealistic macro photograph of an Elephant Beetle (Megasoma elephas), large golden-brown beetle with a long trunk-like horn, covered in fine golden hairs, on a tropical tree trunk, National Geographic style."),
E("彩臂金龟", "Macleay's Long-armed Scarab", "Cheirotonus macleayi",
  "东南亚山地常绿阔叶林", "幼虫腐食朽木,成虫吸食树液",
  "体长约6厘米(含前足可达10厘米)", "6-10克", 0.06, "未评估(NE)", "🪲",
  "雄虫前足极长如臂,鞘翅翠绿泛金属光泽,腹侧缀金黄斑纹,夜间活动于山地森林,是金龟家族中颜值与体态俱佳的珍稀种类。",
  "A photorealistic macro photograph of a Macleay's Long-armed Scarab (Cheirotonus macleayi), metallic green scarab beetle with extremely long front legs and golden markings, on a mossy tree trunk, National Geographic style."),
E("圣甲虫", "Sacred Scarab", "Scarabaeus sacer",
  "地中海沿岸草原与沙地", "成虫与幼虫均以动物粪便为食",
  "体长约3厘米", "1-2克", 0.03, "无危(LC)", "🪲",
  "古埃及人尊崇的圣虫,全身乌黑油亮,以滚动粪球著称,将粪球滚成圆团埋入地下供幼虫食用,被誉为自然界的清道夫与重生象征。",
  "A photorealistic macro photograph of a Sacred Scarab (Scarabaeus sacer), glossy black dung beetle pushing a large dung ball across desert sand, side view, National Geographic style."),
# ---------- 鞘翅目 天牛/吉丁/象鼻虫/锹甲/龙虱 (10) ----------
E("泰坦天牛", "Titan Beetle", "Titanus giganteus",
  "亚马逊雨林", "幼虫蛀食朽木,成虫几乎不进食",
  "体长可达17厘米", "15-25克", 0.17, "未评估(NE)", "🪲",
  "世界最大的甲虫之一,体长可达17厘米,拥有惊人的巨颚与粗壮身体,生活于亚马逊雨林,成虫寿命短暂,习性神秘,难得一见。",
  "A photorealistic macro photograph of a Titan Beetle (Titanus giganteus), enormous dark brown beetle with massive mandibles and a huge armored body, on an Amazonian rainforest tree, National Geographic style."),
E("锯齿天牛", "Saber-tooth Longhorn", "Macrodontia cervicornis",
  "南美洲热带雨林", "幼虫蛀食朽木,成虫取食树液",
  "体长可达15厘米(含颚)", "10-18克", 0.15, "未评估(NE)", "🪲",
  "南美巨型天牛,雄虫下颌形如巨大的锯齿镰刀,体色红褐带黑纹,成虫羽化后主要求偶交配,是昆虫收藏界梦寐以求的传奇物种。",
  "A photorealistic macro photograph of a Saber-tooth Longhorn (Macrodontia cervicornis), giant reddish-brown longhorn beetle with huge curved serrated mandibles, on a rainforest log, National Geographic style."),
E("巨型吉丁虫", "Giant Jewel Beetle", "Megaloxantha bicolor",
  "东南亚热带雨林", "幼虫蛀食树干,成虫取食树液",
  "体长约8厘米", "4-8克", 0.08, "未评估(NE)", "🪲",
  "东南亚最大的吉丁虫,鞘翅翠绿泛金属光泽,腹部缀金黄绒毛,阳光下熠熠生辉,如宝石般璀璨,是甲虫收藏中的顶级珍品。",
  "A photorealistic macro photograph of a Giant Jewel Beetle (Megaloxantha bicolor), large metallic green jewel beetle with golden hairy abdomen and iridescent elytra, on a sunlit tree trunk, National Geographic style."),
E("宝石象鼻虫", "Brazilian Diamond Weevil", "Entimus imperialis",
  "巴西大西洋沿岸雨林", "幼虫蛀食树干,成虫取食树皮与嫩芽",
  "体长约2厘米", "0.3-0.6克", 0.02, "未评估(NE)", "🪲",
  "体表密布金色鳞片,在光线下折射出七彩虹光,宛如镶嵌钻石的珠宝,被称为世界上最璀璨的象鼻虫,是巴西雨林中的活宝石。",
  "A photorealistic macro photograph of a Brazilian Diamond Weevil (Entimus imperialis), weevil covered in iridescent gold and green scales sparkling like diamonds, on a rainforest leaf, National Geographic style."),
E("长颈鹿象鼻虫", "Giraffe Weevil", "Trachelophorus giraffa",
  "马达加斯加东部雨林", "幼虫在卷叶中发育,成虫取食叶片",
  "体长约2.5厘米(雄虫含颈部可达5厘米)", "0.3-0.8克", 0.05, "未评估(NE)", "🪲",
  "马达加斯加特有,雄虫颈部极长形似长颈鹿,通体乌黑带红斑,长颈用于争夺配偶并卷叶筑巢,外形奇异,令人过目难忘。",
  "A photorealistic macro photograph of a Giraffe Weevil (Trachelophorus giraffa), black weevil with red wing covers and an extremely long neck, on a folded leaf in a Madagascan rainforest, National Geographic style."),
E("翡翠象鼻虫", "Schoenherr's Weevil", "Eupholus schoenherri",
  "新几内亚岛雨林", "幼虫蛀食茎干,成虫取食叶片与果实",
  "体长约3厘米", "0.5-1克", 0.03, "未评估(NE)", "🪲",
  "体表覆盖翠绿与天蓝相间的鳞片,间有黑色条纹,色彩艳丽如翡翠与青瓷,是新几内亚雨林中颜值最高的象鼻虫之一。",
  "A photorealistic macro photograph of a Schoenherr's Weevil (Eupholus schoenherri), weevil with brilliant turquoise and emerald green bands and black stripes, on a rainforest stem, National Geographic style."),
E("彩虹锹甲", "Rainbow Stag Beetle", "Phalacrognathus muelleri",
  "澳大利亚东北部雨林", "幼虫腐食朽木,成虫吸食树液与腐果",
  "体长约5厘米", "3-6克", 0.05, "无危(LC)", "🪲",
  "甲虫中的颜值天花板,鞘翅泛七彩金属光泽,如彩虹般绚丽,被誉为最美丽的锹甲,深受世界甲虫爱好者追捧,是澳洲雨林的明星。",
  "A photorealistic macro photograph of a Rainbow Stag Beetle (Phalacrognathus muelleri), metallic beetle with rainbow iridescent elytra and curved mandibles, on a rainforest log, National Geographic style."),
E("黄金鬼锹", "Rosenberg's Stag Beetle", "Allotopus rosenbergi",
  "东南亚热带雨林", "幼虫腐食朽木,成虫吸食树液",
  "体长约6厘米(含颚)", "4-8克", 0.06, "未评估(NE)", "🪲",
  "全身泛金黄色金属光泽,大颚弯曲如镰,宛如黄金铸成的鬼面,是锹甲中的贵族,栖息于东南亚雨林,是收藏界的梦幻品种。",
  "A photorealistic macro photograph of a Rosenberg's Stag Beetle (Allotopus rosenbergi), golden metallic stag beetle with long curved mandibles, on a rainforest branch, National Geographic style."),
E("大龙虱", "Great Diving Beetle", "Dytiscus marginalis",
  "欧洲静水池塘与湖泊", "捕食蝌蚪、小鱼与水生昆虫",
  "体长约3.5厘米", "1-2克", 0.035, "无危(LC)", "🪲",
  "欧洲最大的水生甲虫,体色墨绿带金黄边缘,后足扁平如桨,潜水时随身携带气泡,幼虫凶猛,是淡水生态中的顶级水生猎手。",
  "A photorealistic macro photograph of a Great Diving Beetle (Dytiscus marginalis), dark green water beetle with yellow-bordered elytra and flattened swimming legs, underwater in a pond, National Geographic style."),
# ---------- 直翅目 (3) ----------
E("澳洲巨蚱蜢", "Giant Grasshopper", "Valanga irregularis",
  "澳大利亚北部与东部草原林地", "取食多种草本植物叶片",
  "体长可达9厘米", "8-15克", 0.09, "无危(LC)", "🦗",
  "澳大利亚体型最大的蝗虫,体长可达9厘米,体色黄绿多变,后足强健善跳,飞行能力出众,是澳洲草原上令人惊叹的巨型跳跃高手。",
  "A photorealistic macro photograph of a Giant Grasshopper (Valanga irregularis), huge yellow-green grasshopper with powerful hind legs, perched on a grass blade in the Australian outback, National Geographic style."),
E("沙漠蝗", "Desert Locust", "Schistocerca gregaria",
  "非洲与亚洲干旱半干旱区", "取食禾本科等各类植物",
  "体长约7厘米", "2-4克", 0.07, "无危(LC)", "🦗",
  "世界最著名的迁飞性害虫,群居型单群可达数十亿只,所到之处植被一扫而空,散居型体色斑驳,是草原生态中不可忽视的一环。",
  "A photorealistic macro photograph of a Desert Locust (Schistocerca gregaria), large yellow-brown locust with long wings, on dry desert grass under harsh sunlight, National Geographic style."),
E("巨拟叶螽", "Giant Katydid", "Pseudophyllus titan",
  "东南亚热带雨林", "取食多种树木叶片",
  "体长约8厘米", "10-15克", 0.08, "未评估(NE)", "🦗",
  "世界体型最大的螽斯之一,前翅宽大如叶,翅脉酷似叶片纹理,静止时与树叶浑然一体,是雨林夜间的巨型拟态歌者。",
  "A photorealistic macro photograph of a Giant Katydid (Pseudophyllus titan), enormous green katydid with leaf-like wings and veins, on a tropical rainforest leaf, National Geographic style."),
# ---------- 竹节虫目 (2) ----------
E("澳洲刺竹节虫", "Macleay's Spectre", "Extatosoma tiaratum",
  "澳大利亚东部雨林", "取食桉树与蔷薇科植物叶片",
  "雌虫体长约15厘米", "20-40克", 0.15, "无危(LC)", "🐛",
  "体表布满叶状突起与尖刺,形如带刺的枯枝,雌虫行动迟缓,受惊时摆动模仿风中枝叶,是澳洲雨林中最著名的拟态竹节虫。",
  "A photorealistic macro photograph of a Macleay's Spectre (Extatosoma tiaratum), large brown stick insect covered with leaf-like spines and lobes, on an Australian rainforest branch, National Geographic style."),
E("菲律宾叶䗛", "Philippine Leaf Insect", "Phyllium philippinicum",
  "菲律宾热带雨林", "取食多种阔叶树叶片",
  "体长约7厘米", "6-10克", 0.07, "未评估(NE)", "🐛",
  "外形与绿叶几乎完全一致,翅脉、叶缘甚至虫蚀痕迹一应俱全,静止时就是一片叶子,遇惊晃动模仿风中树叶,拟态技艺登峰造极。",
  "A photorealistic macro photograph of a Philippine Leaf Insect (Phyllium philippinicum), bright green insect shaped exactly like a leaf with veins and bite marks, on a rainforest branch, National Geographic style."),
# ---------- 其他目 (5) ----------
E("帝王蝉", "Imperial Cicada", "Tacua speciosa",
  "东南亚低地雨林", "若虫吸食树根汁液,成虫吸食树液",
  "体长约6厘米,翅展约20厘米", "3-5克", 0.06, "未评估(NE)", "🦗",
  "东南亚最大的蝉类之一,体表墨蓝泛金属光泽,复眼鲜红醒目,翅展近20厘米,叫声嘹亮,被誉为蝉中之王,极具观赏价值。",
  "A photorealistic macro photograph of an Imperial Cicada (Tacua speciosa), large metallic blue-black cicada with bright red eyes and translucent wings, on a rainforest tree trunk, National Geographic style."),
E("巨人豆娘", "Giant Damselfly", "Megaloprepus caerulatus",
  "中美洲雨林林间水潭", "幼虫捕食水生生物,成虫捕食空中飞虫",
  "翅展约19厘米", "1-2克", 0.19, "未评估(NE)", "🪰",
  "世界翅展最大的蜻蜓目昆虫,翅展近19厘米,翅面黑白相间缀蓝色斑纹,飞行缓慢优雅,是中美洲雨林水潭边的空中霸主。",
  "A photorealistic macro photograph of a Giant Damselfly (Megaloprepus caerulatus), huge damselfly with black and white striped wings with blue patches, hovering over a rainforest pool, National Geographic style."),
E("斗牛蚁", "Bull Ant", "Myrmecia pyriformis",
  "澳大利亚东部桉树林地", "捕食昆虫与小动物,也取食花蜜",
  "体长约3厘米", "0.3-0.6克", 0.03, "无危(LC)", "🐜",
  "澳大利亚巨型猛蚁,体型硕大,上颚如钳,毒刺锋利,攻击性极强,视力出众,能跃起反击入侵者,是世界上最危险的蚂蚁之一。",
  "A photorealistic macro photograph of a Bull Ant (Myrmecia pyriformis), large reddish-brown and black ant with huge mandibles and a venomous stinger, on an Australian eucalyptus trunk, National Geographic style."),
E("巨沙螽", "Giant Weta", "Deinacrida heteracantha",
  "新西兰近海岛屿森林", "取食植物叶片、果实与小昆虫",
  "体长约10厘米", "可达70克", 0.1, "易危(VU)", "🦗",
  "新西兰特有,世界最重的昆虫,雌虫体重可达70克,外形如巨型蟋蟀,性情温顺,行动迟缓,是岛屿生态系统中珍贵的活化石。",
  "A photorealistic macro photograph of a Giant Weta (Deinacrida heteracantha), enormous brown cricket-like insect with spiny legs, the heaviest insect in the world, on a mossy forest floor, National Geographic style."),
]

assert len(data) == 40, "count=%d" % len(data)

# ---------- validation ----------
FIELDS = ["name","englishName","scientificName","category","habitat","diet","size","weight","length","status","emoji","description","imagePrompt"]

# existing insects (animals_data.json + new_insects.json) for dedupe
existing_sci, existing_names = set(), set()
for f in ["animals_data.json", "data_batches/new_insects.json"]:
    p = os.path.join(BASE, f)
    if os.path.exists(p):
        d = json.load(open(p, encoding="utf-8"))
        items = d if isinstance(d, list) else d.get("data", [])
        for it in items:
            if "昆虫" in str(it.get("category", "")):
                existing_sci.add(it.get("scientificName", "").strip().lower())
                existing_names.add(it.get("name", "").strip())

errors = []
seen_sci, seen_name = {}, {}
genus_count = {}
for i, it in enumerate(data):
    for k in FIELDS:
        if k not in it:
            errors.append("[%d] missing field %s" % (i, k))
    sc = it["scientificName"].strip().lower()
    nm = it["name"].strip()
    if sc in existing_sci:
        errors.append("[%d] DUPLICATE scientificName vs existing: %s" % (i, it["scientificName"]))
    if nm in existing_names:
        errors.append("[%d] DUPLICATE name vs existing: %s" % (i, nm))
    if sc in seen_sci:
        errors.append("[%d] duplicate within batch: %s" % (i, it["scientificName"]))
    if nm in seen_name:
        errors.append("[%d] duplicate name within batch: %s" % (i, nm))
    seen_sci[sc] = i; seen_name[nm] = i
    g = sc.split()[0]
    genus_count[g] = genus_count.get(g, 0) + 1
    if not (40 <= len(it["description"]) <= 80):
        errors.append("[%d] desc len %d out of 40-80" % (i, len(it["description"])))
    pfx = it["imagePrompt"]
    if not (pfx.startswith("A photorealistic macro photograph of a ") or pfx.startswith("A photorealistic macro photograph of an ")):
        errors.append("[%d] imagePrompt bad prefix" % i)
    if not pfx.endswith("National Geographic style."):
        errors.append("[%d] imagePrompt bad suffix" % i)
    if not isinstance(it["length"], (int, float)):
        errors.append("[%d] length not number" % i)
    if it["category"] != "昆虫类":
        errors.append("[%d] category wrong" % i)

# genus limit: <=2 in THIS batch, and <=2 combined with existing
for g, c in genus_count.items():
    if c > 2:
        errors.append("genus %s appears %d times in batch (>2)" % (g, c))
from collections import Counter
for it in data:
    g = it["scientificName"].split()[0]
    if g in ("Cheirotonus", "Ornithoptera", "Papilio", "Phyllium", "Morpho"):
        # combined count with existing
        tot = sum(1 for s in existing_sci if s.split()[0] == g.lower()) + genus_count.get(g, 0)
        if tot > 2:
            errors.append("genus %s combined count %d > 2" % (g, tot))

if errors:
    print("VALIDATION ERRORS (%d):" % len(errors))
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("OK written %d entries -> %s" % (len(data), OUT))
