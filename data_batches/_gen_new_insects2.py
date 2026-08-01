# -*- coding: utf-8 -*-
"""Generate new_insects2.json: 40 NEW insects, deduplicated against existing data."""
import json, re

OUT = r"C:/Users/Administrator/Desktop/animal-world-mini-program/data_batches/new_insects2.json"
REF_NEW = r"C:/Users/Administrator/Desktop/animal-world-mini-program/data_batches/new_insects.json"
REF_MAIN = r"C:/Users/Administrator/Desktop/animal-world-mini-program/animals_data.json"

def E(name, en, sci, habitat, diet, size, weight, length, status, emoji, desc, ip):
    return {
        "name": name, "englishName": en, "scientificName": sci, "category": "昆虫类",
        "habitat": habitat, "diet": diet, "size": size, "weight": weight,
        "length": length, "status": status, "emoji": emoji,
        "description": desc, "imagePrompt": ip,
    }

P = "A photorealistic macro photograph of a "
NS = " National Geographic style"

data = [
# ============ 鞘翅目 (10) ============
E("桑天牛","Mulberry Longhorn Beetle","Apriona germarii",
  "桑园、果园及阔叶林,幼虫蛀食枝干内部","幼虫蛀食树木枝干木质部,成虫啃食嫩枝树皮",
  "体长3.5-5厘米","约3克",0.045,"无危(LC)","🪲",
  "桑树和果树的重要蛀干害虫,成虫灰褐色密被金黄细毛,触角极长。幼虫蛀食枝干形成隧道,使树势衰弱甚至枯死,是林业与果园重点防治的害虫。",
  P+"Mulberry Longhorn Beetle (Apriona germarii) on a mulberry branch, grey-brown body covered with golden fine hairs, very long antennae, wood-boring damage visible, macro detail,"+NS),
E("桃红颈天牛","Red-necked Longhorn Beetle","Aromia bungii",
  "桃、李、杏、樱桃等核果类果园和林木","幼虫蛀食树干木质部,成虫舔食树液和露水",
  "体长2.8-3.7厘米","约2.5克",0.033,"无危(LC)","🪲",
  "前胸背板鲜红色如系着红围巾,故名桃红颈天牛,是核果类果树的重要蛀干害虫。成虫盛夏出现在树干上,幼虫蛀食木质部形成粗大隧道,严重削弱树势。",
  P+"Red-necked Longhorn Beetle (Aromia bungii) on a peach tree trunk, glossy black body with bright red thorax, long curved antennae, bark texture, macro detail,"+NS),
E("气步甲","Bombardier Beetle","Pheropsophus occipitalis",
  "农田、湿地和林缘地面,昼伏夜出","捕食小型昆虫和蜗牛,也取食腐殖质",
  "体长1.2-1.8厘米","约0.3克",0.015,"无危(LC)","🪲",
  "俗称放屁虫,遇险时从腹部末端喷射高温化学混合液,伴随响声和刺鼻气味,瞬间吓退天敌,是自然界最著名的化学防御专家之一,堪称会开炮的甲虫。",
  P+"Bombardier Beetle (Pheropsophus occipitalis) on forest floor, black body with orange-banded elytra, defensive spray mist at abdomen tip, macro detail,"+NS),
E("大云鳃金龟","Zigzag Chafer","Polyphylla laticollis",
  "山区林地与果园,幼虫(蛴螬)生活在土壤中","幼虫啃食树根,成虫取食树叶",
  "体长2.8-3.5厘米","约2克",0.032,"无危(LC)","🪲",
  "大型鳃金龟,鞘翅上密布白色鳞片组成的云状花纹,因而得名。幼虫蛴螬在地下啃食树根,成虫取食树叶,趋光性强,是山区夜间灯下常见的大型金龟子。",
  P+"Zigzag Chafer (Polyphylla laticollis) on a tree leaf at night, large brown body with white zigzag scale patterns on elytra, lamellate antennae, macro detail,"+NS),
E("椰蛀犀金龟","Coconut Rhinoceros Beetle","Oryctes rhinoceros",
  "热带与亚热带棕榈科植物种植区","幼虫取食腐殖质和朽木,成虫蛀食椰树嫩心与花序",
  "体长3.5-5.5厘米","约5克",0.05,"无危(LC)","🪲",
  "犀金龟亚科大型甲虫,雄性头上有短角,钻蛀椰树嫩心,是热带地区椰子的头号害虫。成虫夜间活动,幼虫在腐殖质中发育,随贸易扩散至全球热带地区。",
  P+"Coconut Rhinoceros Beetle (Oryctes rhinoceros) on a coconut palm trunk, large dark brown body with small horn on head, glossy shell, macro detail,"+NS),
E("丽叩甲","Golden Click Beetle","Campsosternus auratus",
  "松林等针叶林及混交林,幼虫生活在朽木中","幼虫捕食朽木中昆虫,成虫取食树液",
  "体长2.5-3.6厘米","约1克",0.03,"无危(LC)","🪲",
  "体色金绿带铜红色光泽,是叩头虫家族中的颜值担当。受惊时仰面弓身弹跳,发出咔哒声翻身逃跑,幼虫在松树朽木中捕食害虫,是森林生态的重要成员。",
  P+"Golden Click Beetle (Campsosternus auratus) on pine bark, metallic golden-green body with copper reflections, clicking jump posture, macro detail,"+NS),
E("胸窗萤","Chinese Firefly","Pyrocoelia pectoralis",
  "林缘、溪边的草丛和灌丛,幼虫生活在腐殖质丰富的土中","幼虫捕食蜗牛等软体动物,成虫取食露水",
  "体长1.5-2.2厘米","约0.3克",0.018,"无危(LC)","✨",
  "窗萤属代表,前胸背板上有透明小窗,腹部发出黄绿色荧光。雄虫夜间飞行闪烁求偶,幼虫捕食蜗牛,是生态环境良好的指示物种,夏夜山林中流动的星光。",
  P+"Chinese Firefly (Pyrocoelia pectoralis) glowing in the night forest, yellowish-green light from abdomen, transparent window on pronotum, bokeh background,"+NS),
E("锯角萤","Sawtooth Firefly","Vesta impressicollis",
  "山地林间草丛与灌木,幼虫在枯枝落叶层活动","幼虫捕食蜗牛等软体动物,成虫取食露水",
  "体长1-1.5厘米","约0.15克",0.012,"无危(LC)","✨",
  "触角呈锯齿状因而得名,夏夜在低空缓缓飞行,腹部发出柔和的黄绿荧光。幼虫在枯枝落叶中捕食蜗牛,成虫寿命短暂,是山野夏夜浪漫风景的缔造者。",
  P+"Sawtooth Firefly (Vesta impressicollis) on a leaf at dusk, serrate antennae, soft yellow-green glow from abdomen, dark background, macro detail,"+NS),
E("大龙虱","Great Diving Beetle","Dytiscus marginalis",
  "池塘、湖泊等静水水域,善于游泳","捕食小鱼、蝌蚪、水生昆虫等",
  "体长2.7-3.5厘米","约2克",0.031,"无危(LC)","🪲",
  "体型最大的龙虱之一,后足特化成桨状,在水下飞速划行捕食小鱼和蝌蚪。鞘翅下携带空气泡潜入水底呼吸,幼虫凶猛,是池塘生态系统的顶级水生捕食者。",
  P+"Great Diving Beetle (Dytiscus marginalis) underwater in a pond, dark olive body with yellow margins, paddle-like hind legs, air bubble trapped under elytra,"+NS),
E("拉步甲","Lafosse's Ground Beetle","Carabus lafossei",
  "山地林间地面,昼伏夜出","捕食蜗牛、毛虫等小型动物",
  "体长3.5-4.5厘米","约1.8克",0.04,"近危(NT)","🪲",
  "我国珍稀步甲,鞘翅金绿色带虹彩,华丽夺目。它昼伏夜出,在林中地面捕食蜗牛和毛虫,是国家二级保护动物,被誉为行走的宝石,十分珍贵。",
  P+"Lafosse's Ground Beetle (Carabus lafossei) on mossy forest floor, iridescent metallic green and gold elytra, long legs, dew drops, macro detail,"+NS),
# ============ 鳞翅目 (4) ============
E("野蚕","Wild Silkworm Moth","Bombyx mandarina",
  "桑园及野生桑树林,幼虫在桑叶上取食","幼虫取食桑叶,成虫口器退化不取食",
  "体长2.5-3厘米,翅展4-5厘米","约1克",0.03,"无危(LC)","🐛",
  "家蚕的近缘野生种,也是家蚕驯化的重要祖先。幼虫深褐色取食桑叶,茧小而硬,成虫深褐色带黑色波纹。研究野蚕对理解蚕丝业起源具有重要科学价值。",
  P+"Wild Silkworm Moth (Bombyx mandarina) resting on a mulberry leaf, dark brown wings with wavy black lines, furry body, macro detail,"+NS),
E("樗蚕","Ailanthus Silkmoth","Samia cynthia",
  "臭椿、乌桕等树木,幼虫在寄主叶片上取食","幼虫取食臭椿等叶片,成虫口器退化不取食",
  "翅展11-14厘米","约2.5克",0.12,"无危(LC)","🦋",
  "幼虫以臭椿树叶为食,成虫翅展可达14厘米,翅面淡褐色,中央有白色月牙纹。其茧可缫丝,而由它驯化而来的蓖麻蚕在印度等地大量饲养,是重要的经济昆虫。",
  P+"Ailanthus Silkmoth (Samia cynthia) on a tree branch, large fawn-brown wings with white crescent markings, feathery antennae, macro detail,"+NS),
E("绿尾大蚕蛾","Indian Moon Moth","Actias selene",
  "阔叶林地与果园,幼虫取食柳树、樟树等叶片","幼虫取食多种树木叶片,成虫不取食",
  "翅展11-15厘米","约3克",0.13,"无危(LC)","🦋",
  "大型天蚕蛾,翅粉绿色,后翅拖出修长的燕尾状尾突,紫红色月牙斑醒目,被誉为月神蛾。幼虫取食柳树、樟树等叶片,夜间趋光,是蛾类中的颜值巅峰。",
  P+"Indian Moon Moth (Actias selene) with pale green wings and long trailing tails perched on a leaf, purple eye spots, soft light, macro detail,"+NS),
E("甘薯天蛾","Sweet Potato Hawkmoth","Agrius convolvuli",
  "农田、菜地及旷野,幼虫取食甘薯等旋花科植物","幼虫取食甘薯叶片,成虫吸食花蜜",
  "翅展9-11厘米","约1.5克",0.1,"无危(LC)","🦋",
  "幼虫俗称猪儿虫,专吃甘薯叶片,是薯类作物的重要害虫。成虫翅灰褐色带云纹,后翅有黑白相间斑带,飞行迅速,常在黄昏吸食花蜜,迁飞能力强。",
  P+"Sweet Potato Hawkmoth (Agrius convolvuli) hovering at a flower at dusk, grey marbled forewings, pink and black banded hindwings, long proboscis,"+NS),
# ============ 膜翅目 (5) ============
E("松毛虫黑胸姬蜂","Pine-caterpillar Ichneumon","Hyposoter takagii",
  "松林及针叶林地","幼虫寄生于松毛虫幼虫体内,成虫吸食花蜜",
  "体长1-1.5厘米","约0.05克",0.012,"无危(LC)","🐝",
  "马尾松毛虫的天敌,雌蜂把卵产进松毛虫幼虫体内,后代在寄主体内发育使其死亡。它是我国松林生物防治的重要寄生蜂资源,默默守护着松林的健康。",
  P+"Pine-caterpillar Ichneumon (Hyposoter takagii) on a pine needle, slender black body with reddish legs, long ovipositor, transparent wings, macro detail,"+NS),
E("螟蛉绒茧蜂","Rufous Braconid Wasp","Cotesia ruficrus",
  "稻田、棉田等农作物环境","幼虫寄生于螟虫等害虫幼虫体内,成虫吸食花蜜",
  "体长约3毫米","约0.005克",0.003,"无危(LC)","🐝",
  "体型微小却本领高强的寄生蜂,雌蜂将卵产入螟虫幼虫体内,后代在寄主体表结成白色小茧。它寄生稻螟、棉铃虫等多种害虫,是稻田生物防治的功臣。",
  P+"Rufous Braconid Wasp (Cotesia ruficrus) on a rice leaf, tiny black body with red-brown abdomen, white cocoon cluster on a caterpillar nearby, macro detail,"+NS),
E("蜾蠃","Potter Wasp","Eumenes pomiformis",
  "山坡、林缘和屋檐下,独居筑巢","捕猎鳞翅目幼虫贮巢育幼,成虫吸食花蜜",
  "体长1.5-2厘米","约0.2克",0.018,"无危(LC)","🐝",
  "俗称细腰蜂,独居胡蜂,用泥土筑成坛子状小巢,捕猎尺蠖等幼虫麻醉后贮入巢中供后代食用。古人误以为它收养螟蛉为子,留下螟蛉有子的典故。",
  P+"Potter Wasp (Eumenes pomiformis) building a mud pot nest on a wall, black and yellow banded waist, mud pot with round opening, macro detail,"+NS),
E("苜蓿切叶蜂","Alfalfa Leafcutter Bee","Megachile rotundata",
  "农田、果园和荒地,在土穴或空心茎秆中筑巢","成虫采食花蜜和花粉,用切下的叶片筑巢",
  "体长约1厘米","约0.08克",0.01,"无危(LC)","🐝",
  "著名独居蜂,雌蜂用大颚把叶片切成整齐的椭圆片,卷成巢室产卵并贮备花粉。它是苜蓿授粉的主力,效率远超蜜蜂,已被人工饲养用于牧草种子生产。",
  P+"Alfalfa Leafcutter Bee (Megachile rotundata) carrying a cut leaf piece on an alfalfa flower, dark body with pale bands, scopa hairs under abdomen, macro detail,"+NS),
E("青蜂","Ruby-tailed Wasp","Chrysis ignita",
  "向阳的墙缝、木桩和废弃巢穴附近","幼虫寄生于其他独居蜂巢中,成虫取食花蜜",
  "体长0.6-1.2厘米","约0.05克",0.009,"无危(LC)","🐝",
  "体色翠蓝带金属光泽,如宝石般耀眼,俗称青蜂。雌蜂把卵产进其他独居蜂的巢中,幼虫吃掉寄主幼虫和食物,是典型的巢寄生昆虫,飞行敏捷。",
  P+"Ruby-tailed Wasp (Chrysis ignita) on a wooden post, brilliant metallic blue-green body with ruby-red abdomen tip, sparkling iridescence, macro detail,"+NS),
# ============ 双翅目 (4) ============
E("白纹伊蚊","Asian Tiger Mosquito","Aedes albopictus",
  "城市与乡村的积水容器、竹筒、轮胎等小水体","雌蚊吸血,也吸食花蜜等植物汁液",
  "体长约0.5厘米","约0.002克",0.005,"无危(LC)","🦟",
  "俗称花蚊子,身体黑白相间,白天也攻击人,是登革热等疾病的主要传播媒介。它喜欢在瓶罐积水等小型水体产卵,卵耐旱耐寒,城市居民区是繁殖温床。",
  P+"Asian Tiger Mosquito (Aedes albopictus) on human skin, black body with white stripes, needle-like proboscis, fine scales on wings, macro detail,"+NS),
E("淡色库蚊","Common House Mosquito","Culex pipiens pallens",
  "污水沟、池塘等富含有机质的水体附近","雌蚊吸食人畜血液,雄蚊吸食花蜜",
  "体长约0.5厘米","约0.002克",0.005,"无危(LC)","🦟",
  "我国城镇最常见的家蚊,黄昏后入室叮人吸血,是传播流行性乙型脑炎的重要媒介。它偏爱污水等有机质丰富的水体繁殖,幼虫孑孓倒悬水面呼吸。",
  P+"Common House Mosquito (Culex pipiens pallens) resting on a wall, pale brown body, striped legs, transparent wings, macro detail,"+NS),
E("红头丽蝇","Common Bluebottle Fly","Calliphora vicina",
  "城镇与乡村,幼虫孳生于腐败有机物中","成虫取食腐烂物质和花蜜,幼虫以腐肉为食",
  "体长0.8-1.4厘米","约0.06克",0.011,"无危(LC)","🪰",
  "头胸带蓝绿色金属光泽,常见于腐败物质附近。幼虫在动物尸体上取食,加速有机物分解,在法医学中可依据其发育阶段推算死亡时间,是重要的法医昆虫。",
  P+"Common Bluebottle Fly (Calliphora vicina) on a leaf, blue-green metallic thorax, red eyes, fine bristles, macro detail,"+NS),
E("丝光绿蝇","Common Green Bottle Fly","Lucilia sericata",
  "垃圾堆、动物尸体、粪便等腐败场所","成虫取食腐殖质和花蜜,幼虫以腐败有机物为食",
  "体长0.6-1厘米","约0.04克",0.008,"无危(LC)","🪰",
  "体呈金绿色金属光泽,是绿蝇属的代表。幼虫在腐败物或伤口中取食,经严格消毒的幼虫可用于清除创面坏死组织,即蛆疗,是医学上以虫治病的经典案例。",
  P+"Common Green Bottle Fly (Lucilia sericata) on a white flower, shiny metallic green body, red compound eyes, translucent wings, macro detail,"+NS),
# ============ 蜻蜓目 (3) ============
E("东亚异痣蟌","Asian Bluetail Damselfly","Ischnura asiatica",
  "池塘、水田、溪流边的水生植物上","捕食蚊蝇等小型飞虫",
  "体长约3厘米","约0.05克",0.03,"无危(LC)","🦗",
  "蟌科豆娘,身体纤细,雄虫腹部末端带蓝色斑,停歇时四翅合拢竖立。稚虫在水中捕食孑孓,成虫在水边草丛捕食蚊蝇,是池塘边优雅的小直升机。",
  P+"Asian Bluetail Damselfly (Ischnura asiatica) perched on a reed stem, slender blue-green body with blue tail segment, wings folded upright, water reflection,"+NS),
E("玉带蜻","Banded Skimmer","Pseudothemis zonata",
  "池塘、湖泊等静水水域附近","捕食蚊蝇等小型飞虫",
  "体长约4厘米","约0.25克",0.04,"无危(LC)","🦗",
  "雄虫腹部有醒目的白色环带,像系着玉带,飞行时十分显眼。它常在池塘水面上空巡飞,捕食蚊虫,停歇时翅膀平展,是城市公园水边最常见的蜻蜓之一。",
  P+"Banded Skimmer (Pseudothemis zonata) hovering above a pond, black body with prominent white band, transparent wings with dark base, water surface,"+NS),
E("大团扇春蜓","Chinese Clubtail Dragonfly","Sinictinogomphus clavatus",
  "溪流、池塘等水域附近,常停歇在岸边","捕食蚊蝇等飞虫,稚虫捕食水生昆虫",
  "体长7-8厘米","约0.8克",0.075,"无危(LC)","🦗",
  "春蜓科大型蜻蜓,腹部末端膨大如扇,黑黄相间,十分威武。稚虫水虿潜伏水底泥沙中捕食,成虫常在溪流池塘边巡飞,是南方水域的空中霸主。",
  P+"Chinese Clubtail Dragonfly (Sinictinogomphus clavatus) resting on a streamside rock, black and yellow banded body with club-shaped tail, large green eyes,"+NS),
# ============ 直翅目 (3) ============
E("双斑蟋","Two-spotted Cricket","Gryllus bimaculatus",
  "草丛、农田和砖石缝隙,夜间活动","取食植物嫩叶、根茎及小型昆虫",
  "体长2-2.6厘米","约0.6克",0.023,"无危(LC)","🦗",
  "前胸背板两侧各有一个黄白色斑,故名双斑蟋。它栖息于草丛和农田,雄虫夜间鸣叫悦耳,是常见的观赏鸣虫,也取食植物嫩叶,全球分布广泛。",
  P+"Two-spotted Cricket (Gryllus bimaculatus) at the entrance of its burrow in soil, shiny black body with two yellow spots on wing base, long antennae, macro detail,"+NS),
E("绿螽斯","Great Green Bush-cricket","Tettigonia viridissima",
  "灌丛、草丛和农田,栖息在植物上","捕食昆虫,也取食植物嫩叶",
  "体长3.5-4.5厘米","约1.5克",0.04,"无危(LC)","🦗",
  "通体翠绿,体长达4厘米,是常见的大型螽斯。雄虫摩擦前翅发出响亮鸣声,捕食昆虫也吃植物,是草丛中的伏击高手,一身绿色军装隐蔽性极佳。",
  P+"Great Green Bush-cricket (Tettigonia viridissima) on a green leaf, vivid green body, very long antennae, large jumping legs, macro detail,"+NS),
E("亚洲小车蝗","Asiatic Grasshopper","Oedaleus asiaticus",
  "草原、农田和山坡草地","取食禾本科牧草和作物叶片",
  "体长2.5-3.5厘米","约0.8克",0.03,"无危(LC)","🦗",
  "我国草原和农田的常见蝗虫,体黄褐色,前翅有黑色斑纹,后足胫节红色。发生量大时可成群迁飞,啃食牧草和庄稼,是草原生态监测的重点害虫。",
  P+"Asiatic Grasshopper (Oedaleus asiaticus) on grassland, yellow-brown body with black markings on forewings, red hind tibia, macro detail,"+NS),
# ============ 半翅目 (5) ============
E("温带臭虫","Common Bed Bug","Cimex lectularius",
  "人类居所的床板、墙缝、家具缝隙中","夜间吸食人血",
  "体长约0.5厘米","约0.05克",0.005,"无危(LC)","🪳",
  "俗称臭虫,身体扁椭圆形红褐色,白天藏匿床缝墙缝,夜间爬出吸食人血,叮咬处奇痒难忍。它耐饥饿能力极强,可数月不食,是与人伴生的吸血害虫。",
  P+"Common Bed Bug (Cimex lectularius) on a mattress seam, flat oval reddish-brown body, small head with piercing mouthparts, macro detail,"+NS),
E("茶翅蝽","Brown Marmorated Stink Bug","Halyomorpha halys",
  "果园、菜地和行道树,常栖息在枝叶上","刺吸苹果、梨等果实和叶片汁液",
  "体长1.2-1.6厘米","约0.3克",0.014,"无危(LC)","🪲",
  "褐灰色体表密布细刻点,臭腺发达,受惊散发难闻气味。它刺吸苹果、梨等果实汁液,造成果面凹陷畸形,是果园重要害虫,原产东亚现已入侵欧美。",
  P+"Brown Marmorated Stink Bug (Halyomorpha halys) on a pear fruit, mottled brown shield-shaped body, banded antennae and legs, macro detail,"+NS),
E("鸣鸣蝉","Black-winged Cicada","Hyalessa maculaticollis",
  "山地树林与果园,幼虫在地下吸食树根汁液","若虫吸食树根汁液,成虫刺吸树干汁液",
  "体长3.5-4厘米","约0.9克",0.038,"无危(LC)","🦗",
  "夏日山林最常见的鸣蝉,体黑褐色,前翅基半部黑色。雄蝉在午后发出响亮的鸣叫,声震林间,幼虫在地下生活数年,羽化后蜕壳高歌,是夏天的标志声音。",
  P+"Black-winged Cicada (Hyalessa maculaticollis) on a tree trunk, black-brown body, dark basal half of wings, large compound eyes, summer forest background,"+NS),
E("红娘子","Red Cicada","Huechys sanguinea",
  "山地灌丛和林缘,若虫在地下吸食树根汁液","若虫吸食树根汁液,成虫刺吸枝干汁液",
  "体长2-2.5厘米","约0.4克",0.022,"无危(LC)","🦗",
  "全身朱红色,翅黑色,色彩对比鲜明,是蝉中的明星。它栖息于山地灌丛,若虫在地下吸食树根汁液,成虫期短,干燥虫体是传统中药材,名为红娘子。",
  P+"Red Cicada (Huechys sanguinea) on a twig, striking scarlet body with black wings, vivid color contrast, macro detail,"+NS),
E("褐飞虱","Brown Planthopper","Nilaparvata lugens",
  "水稻田,群集在稻株基部","刺吸水稻茎秆汁液",
  "体长3-4毫米","约0.001克",0.0035,"无危(LC)","🦗",
  "水稻最严重的迁飞性害虫,体黄褐至暗褐色,群集稻丛基部刺吸汁液,大发生时稻株枯黄倒伏,俗称虱烧。每年随气流从南方迁飞北上,是稻区重点监测对象。",
  P+"Brown Planthopper (Nilaparvata lugens) on a rice stem base, small brown insect with wedge-shaped wings, rice paddy background, macro detail,"+NS),
# ============ 竹节虫目 (1) ============
E("枝䗛","Pink-winged Stick Insect","Sipyloidea sipylus",
  "热带、亚热带灌丛和林地,停歇在枝条上","取食蔷薇科、豆科等多种植物叶片",
  "体长7-9厘米","约3克",0.08,"无危(LC)","🦗",
  "竹节虫目枝䗛,身体细长如枯枝,连颜色和姿态都模仿树枝,静止时几乎无法分辨。雌虫翅退化,卵酷似植物种子,是拟态与伪装艺术的极致体现。",
  P+"Pink-winged Stick Insect (Sipyloidea sipylus) mimicking a twig on a branch, slender stick-like brown body, folded legs, camouflage perfection, macro detail,"+NS),
# ============ 螳螂目 (1) ============
E("眼斑螳","Jeweled Flower Mantis","Creobroter gemmatus",
  "林缘灌丛和花丛,常在花朵间活动","捕食蜜蜂、蝴蝶等访花昆虫",
  "体长3-4厘米","约1克",0.035,"无危(LC)","🦗",
  "前翅上有酷似眼睛的斑纹,遇敌时展翅亮出吓退捕食者。它体型小巧,常在花间伏击蜜蜂蝴蝶,若虫爬行姿态如蚂蚁,是花卉上优雅的伏击猎手。",
  P+"Jeweled Flower Mantis (Creobroter gemmatus) on a white flower, pale green body with eye-like spots on wings, raptorial forelegs, macro detail,"+NS),
# ============ 蜚蠊目 (1) ============
E("东方蜚蠊","Oriental Cockroach","Blatta orientalis",
  "住宅、地下室等阴暗潮湿处,夜行性","取食各种有机物,包括食物残渣和垃圾",
  "体长2.5-3厘米","约0.8克",0.028,"无危(LC)","🪳",
  "原产亚洲的蟑螂,体黑褐色有光泽,俗称黑蟑螂。它喜阴暗潮湿环境,夜行性,取食各种有机物,是城市和住宅常见的卫生害虫,雌虫产卵于坚硬的卵鞘中。",
  P+"Oriental Cockroach (Blatta orientalis) on a dark damp wall corner, glossy dark brown-black body, long antennae, flattened body, macro detail,"+NS),
# ============ 等翅目 (1) ============
E("黄翅大白蚁","Yellow-winged Termite","Macrotermes barneyi",
  "我国南方林地、田埂和房屋地基,地下筑巢","工蚁取食枯木、木材和农作物",
  "体长1.3-1.8厘米","约0.1克",0.015,"无危(LC)","🐜",
  "我国南方最常见的土栖白蚁,工蚁和兵蚁分工明确,在地下筑成庞大的蚁巢和蚁道。它取食枯木和农作物,能蛀空房屋木构件,是建筑与农林的重要害虫。",
  P+"Yellow-winged Termite (Macrotermes barneyi) soldier termite on a mound, pale yellow body with large dark head and mandibles, worker termites around,"+NS),
# ============ 缨尾目 (1) ============
E("衣鱼","Silverfish","Lepisma saccharina",
  "室内温暖潮湿处,如书房、衣柜、浴室","取食纸张、衣物、淀粉和糖类",
  "体长约1厘米","约0.02克",0.01,"无危(LC)","🐛",
  "古老的原始昆虫,身体扁平银灰色,密被鳞片,行动时如一条银鱼游动。它喜欢温暖潮湿处,取食纸张、衣物和淀粉,常在书房衣柜出现,是伴人昆虫之一。",
  P+"Silverfish (Lepisma saccharina) on an old book page, elongated silvery body covered with scales, three tail filaments, antennae, macro detail,"+NS),
# ============ 脉翅目 (1) ============
E("中华草蛉","Chinese Green Lacewing","Chrysoperla nipponensis",
  "农田、果园和林缘草丛","幼虫捕食蚜虫等害虫,成虫取食花蜜和蜜露",
  "体长1-1.5厘米","约0.05克",0.012,"无危(LC)","🐛",
  "通体草绿色,复眼金色,翅脉如细网。幼虫俗称蚜狮,专捕蚜虫、介壳虫,一头幼虫一生可消灭数百只蚜虫,是农田生物防治中不可或缺的重要天敌。",
  P+"Chinese Green Lacewing (Chrysoperla nipponensis) on a wheat leaf, delicate green body with golden eyes, translucent veined wings, macro detail,"+NS),
]

# ---------- validation ----------
assert len(data) == 40, f"count={len(data)}"
names = [d["name"] for d in data]
scis = [d["scientificName"] for d in data]
assert len(set(names)) == 40, "duplicate name"
assert len(set(scis)) == 40, "duplicate scientificName"

# collect all existing scientific names (main 300 + other batch 120)
existing = set()
for f in (REF_MAIN, REF_NEW):
    with open(f, encoding="utf-8") as fh:
        j = json.load(fh)
    items = j["animals"] if isinstance(j, dict) and "animals" in j else j
    for it in items:
        if it.get("category") == "昆虫类" and it.get("scientificName"):
            existing.add(it["scientificName"].strip().lower())
print("existing insect sci names in refs:", len(existing))

dup = [d["scientificName"] for d in data if d["scientificName"].strip().lower() in existing]
assert not dup, f"duplicates with existing: {dup}"

# genus limit: <=2 per genus across existing + new
genus_count = {}
for s in existing:
    g = s.split()[0]
    genus_count[g] = genus_count.get(g, 0) + 1
for d in data:
    g = d["scientificName"].split()[0]
    genus_count[g] = genus_count.get(g, 0) + 1
over = {g: c for g, c in genus_count.items() if c > 2 and g in [d["scientificName"].split()[0] for d in data]}
assert not over, f"genus >2: {over}"

REQ = ["name","englishName","scientificName","category","habitat","diet","size","weight","length","status","emoji","description","imagePrompt"]
for i, d in enumerate(data):
    for k in REQ:
        assert k in d and d[k] not in (None, ""), f"#{i} missing {k}"
    assert d["category"] == "昆虫类"
    assert 40 <= len(d["description"]) <= 80, f"#{i} desc len {len(d['description'])}: {d['name']}"
    assert d["imagePrompt"].startswith("A photorealistic macro photograph of a "), f"#{i} ip prefix"
    assert d["imagePrompt"].endswith("National Geographic style"), f"#{i} ip suffix"
    assert isinstance(d["length"], (int, float)), f"#{i} length type"

with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=1)

print("OK wrote", OUT)
print("count:", len(data))
print("desc lengths:", [len(d["description"]) for d in data])
print("genus within batch:", sorted(set(d["scientificName"].split()[0] for d in data)))
