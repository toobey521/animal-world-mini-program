#!/usr/bin/env node
/**
 * 动物数据管理脚本 - 用于扩展和整理动物数据库
 * 使用方法：node manage_animals.js [命令] [参数]
 */

const fs = require('fs');
const path = require('path');

class AnimalDataManager {
    constructor(dataFile = 'animals_data.json') {
        this.dataFile = path.join(__dirname, dataFile);
        this.animals = this.loadAnimals();
    }

    loadAnimals() {
        if (fs.existsSync(this.dataFile)) {
            const data = fs.readFileSync(this.dataFile, 'utf8');
            return JSON.parse(data).animals || [];
        }
        // 初始化一些示例数据
        return [
            {
                name: '大熊猫',
                category: '哺乳类',
                scientificName: 'Ailuropoda melanoleuca',
                habitat: '中国四川、陕西、甘肃的山区竹林',
                diet: '主要以竹子为食（99%），偶尔吃小型动物和鸟类',
                size: '体长60-85cm，体重85-125kg',
                weight: '100kg',
                length: '0.7m',
                status: '易危（VU）',
                imagePlaceholder: 'panda.jpg',
                description: '中国的国宝，黑白相间，以竹子为主食，憨态可掬。世界自然基金会的标志性动物，也是濒危物种保护的象征。'
            },
            {
                name: '金丝猴',
                category: '哺乳类',
                scientificName: 'Rhinopithecus roxellanae',
                habitat: '中国西南和中部的高山森林（海拔2200-3400米）',
                diet: '水果、树叶、种子、树皮和昆虫',
                size: '体长约75cm，尾长与身长相等',
                weight: '10-15kg',
                length: '0.75m',
                status: '濒危（EN）',
                imagePlaceholder: 'goldenmonkey.jpg',
                description: '毛发金黄如丝，面部蓝色，是中国特有的珍稀灵长类动物，生活在高海拔地区。'
            }
        ];
    }

    saveAnimals() {
        const data = {
            version: '1.0',
            generatedAt: new Date().toISOString(),
            animals: this.animals
        };
        fs.writeFileSync(this.dataFile, JSON.stringify(data, null, 2), 'utf8');
        console.log(`✓ 已保存 ${this.animals.length} 种动物的数据到 ${this.dataFile}`);
    }

    addAnimal(animal) {
        animal.id = animal.id || Date.now() + Math.floor(Math.random() * 1000);
        this.animals.push(animal);
        this.saveAnimals();
        console.log(`✓ 已添加新动物：${animal.name}`);
    }

    bulkAdd(animals) {
        animals.forEach(animal => this.addAnimal(animal));
        console.log(`✓ 已批量添加 ${animals.length} 种动物`);
    }

    getByName(name) {
        return this.animals.find(a => a.name === name);
    }

    getByCategory(category) {
        return this.animals.filter(a => a.category === category);
    }

    getStatusList() {
        const statuses = {};
        this.animals.forEach(a => {
            statuses[a.status] = (statuses[a.status] || 0) + 1;
        });
        return statuses;
    }

    generateExport() {
        const exportData = {
            version: '1.0',
            timestamp: new Date().toISOString(),
            totalAnimals: this.animals.length,
            categories: [...new Set(this.animals.map(a => a.category))],
            animals: this.animals.map(a => ({
                name: a.name,
                category: a.category,
                scientificName: a.scientificName,
                description: `${a.habitat}。${a.diet}。体型：${a.size}。保护级别：${a.status}`
            }))
        };

        const outputPath = path.join(__dirname, 'animal_export.json');
        fs.writeFileSync(outputPath, JSON.stringify(exportData, null, 2), 'utf8');
        console.log(`✓ 导出数据文件生成：${outputPath}`);
        return exportData;
    }

    // 从CSV格式导入数据（核心功能！支持1000种动物批量导入）
    async importFromCsv(csvFilePath) {
        try {
            const csvData = fs.readFileSync(csvFilePath, 'utf8');
            const lines = csvData.trim().split('\n');

            if (lines.length < 2) {
                throw new Error('CSV 文件格式错误或为空！请确保包含表头和至少一条记录。');
            }

            const headers = lines[0].split(',').map(h => h.trim());
            console.log(`\n📊 正在解析 CSV 文件... 共 ${lines.length - 1} 条数据记录`);
            console.log('📋 字段:', headers.join(' | '));

            const imported = [];
            const requiredFields = ['name', 'category'];

            for (let i = 1; i < lines.length; i++) {
                const values = lines[i].split(',');

                if (values.length !== headers.length) {
                    console.warn(`⚠️ 第 ${i + 1} 行字段数不匹配，跳过这条记录`);
                    continue;
                }

                const animal = {};
                let isValid = true;

                headers.forEach((header, idx) => {
                    animal[header] = values[idx].trim();
                });

                // 验证必需字段
                requiredFields.forEach(field => {
                    if (!animal[field] || animal[field] === '') {
                        console.error(`✗ 缺少必需的字段 "${field}" (ID: ${animal.id || i})`);
                        isValid = false;
                    }
                });

                if (!isValid) {
                    console.log(`   跳过无效记录`);
                    continue;
                }

                // 设置默认值如果缺失
                if (!animal.scientificName) animal.scientificName = '';
                if (!animal.habitat) animal.habitat = '未知';
                if (!animal.diet) animal.diet = '未知';
                if (!animal.size) animal.size = '未知';
                if (!animal.weight) animal.weight = '未知';
                if (!animal.length) animal.length = '未知';
                if (!animal.status) animal.status = '无危';
                if (!animal.imagePlaceholder) animal.imagePlaceholder = `animal_${animal.id || i}.jpg`;
                if (!animal.description) animal.description = '暂无描述';
                if (!animal.emoji) animal.emoji = '🐾';

                imported.push(animal);
            }

            console.log(`\n✅ 成功解析 ${imported.length} 条有效数据`);

            // 确认是否导入
            if (imported.length > 0) {
                const confirm = await this.confirmAction(`确定要将这 ${imported.length} 种动物添加到数据库中吗？（Y/N）`);
                if (confirm) {
                    this.bulkAdd(imported);
                    this.saveAnimals();
                    console.log(`\n🎉 导入成功！现在共有 ${this.animals.length} 种动物了！`);
                    this.showImportSummary(imported);
                } else {
                    console.log('❌ 导入被用户取消');
                }
            } else {
                console.log('⚠️ 没有找到有效的数据进行导入');
            }

            return imported;
        } catch (error) {
            console.error('❌ CSV 导入失败:', error.message);
            throw error;
        }
    }

    showImportSummary(newAnimals) {
        const categories = {};
        newAnimals.forEach(a => {
            categories[a.category] = (categories[a.category] || 0) + 1;
        });

        console.log('\n📈 按分类统计：');
        Object.entries(categories).sort().forEach(([cat, count]) => {
            console.log(`   ${cat}: ${count} 种`);
        });
    }

    confirmAction(prompt) {
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        return new Promise(resolve => {
            rl.question(prompt, (answer) => {
                rl.close();
                resolve(answer.toUpperCase() === 'Y');
            });
        });
    }

    bulkGenerateSampleAnimals(count = 1000) {
        // 生成模拟动物数据
        const sampleAnimaless = [];
        const categories = ['哺乳类', '鸟类', '鱼类', '爬行类', '两栖类', '甲壳类', '软体类'];
        const names = ['龙', '凤', '麒麟', '貔貅', '饕餮', '毕方', '梼杌', '混沌', '穷奇',
                       '虎', '狮', '豹', '狼', '狐', '兔', '鼠', '猴', '猪', '狗', '牛', '羊', '马',
                       '鹰', '鹤', '鹅', '鸭', '鸡', '孔雀', '鹦鹉', '天鹅', '燕子', '鸽子', '蜜蜂',
                       '蝴蝶', '蜻蜓', '蜘蛛', '蜗牛', '蚯蚓', '蜈蚣', '蝎子', '螃蟹', '章鱼', '海豚',
                       '海龟', '鲨鱼', '金鱼', '鲤鱼', '鲑鱼', '鲸鱼', '企鹅', '考拉', '袋鼠',
                       '熊猫', '猴子', '大象', '长颈鹿', '斑马', '河马', '犀牛', '骆驼', '羚羊', '牦牛',
                       '恐龙', '猛犸象', '剑齿虎', '渡渡鸟', '袋狼', '旅鸽'];

        for (let i = 1; i <= count; i++) {
            const randomCategory = categories[Math.floor(Math.random() * categories.length)];
            const baseName = names[Math.floor(Math.random() * names.length)] || `动物${i}`;
            const name = `${baseName}${i > 10 ? '_' + i : ''}`;

            sampleAnimaless.push({
                id: i,
                name: name,
                scientificName: `${randomCategory}_${i}`,
                category: randomCategory,
                habitat: `栖息地描述${i}`,
                diet: '食物描述${i}',
                size: `体型${i}描述`,
                weight: `${Math.floor(Math.random() * 1000)}kg`,
                length: `${(Math.random() * 5).toFixed(2)}m`,
                status: ['极危', '濒危', '易危', '近危', '无危'][Math.floor(Math.random() * 5)],
                imagePlaceholder: `${name.toLowerCase().replace(/[^a-z0-9]/g, '_')}.jpg`,
                description: `这是第${i}种动物的介绍。分类：${randomCategory}。体型：${size}。属于${status}物种。`,
                emoji: ['🐾', '🐶', '🐱', '🦁', '🐯', '🐻', '🐼', '🐨', '🦘', '🦝', '🦡', '🦦'][Math.floor(Math.random() * 12)]
            });
        }

        return sampleAnimaless;
    }

    // 交互式添加动物
    async handleAddCommand(rl) {
        console.log('\n=== 添加新动物 ===\n');

        const name = await this.askQuestion(rl, '动物名称（中文）：');
        const category = await this.askQuestion(rl, '分类（如：哺乳类/鸟类/鱼类）：');
        const scientific = await this.askQuestion(rl, '拉丁学名（可选）：');
        const habitat = await this.askQuestion(rl, '栖息地：');
        const diet = await this.askQuestion(rl, '食性：');
        const size = await this.askQuestion(rl, '体型特征：');
        const status = await this.askQuestion(rl, '保护级别（极危/濒危/易危/近危/无危等）：');
        const image = await this.askQuestion(rl, '图片文件名（如panda.jpg）：');
        const desc = await this.askQuestion(rl, '动物简介（回车跳过）：');

        this.addAnimal({
            name,
            category,
            scientificName: scientific || '',
            habitat,
            diet,
            size,
            status,
            imagePlaceholder: image || `${name}.jpg`,
            description: desc || '暂无描述'
        });

        rl.close();
    }

    async askQuestion(rl, prompt) {
        return new Promise(resolve => {
            rl.question(prompt, (answer) => resolve(answer));
        });
    }
}

// CLI 主函数
async function main() {
    const manager = new AnimalDataManager();
    const args = process.argv;

    // 没有参数时显示帮助
    if (args.length <= 2) {
        showHelp();
        return;
    }

    const command = args[2];
    const param = args[3];

    switch (command) {
        case '--stats':
            console.log('\n=== 数据统计 ===');
            console.log(`总物种数：${manager.animals.length}`);
            const categories = new Set(manager.animals.map(a => a.category));
            console.log(`分类数量：${categories.size}`);
            console.log('各分类数量：');
            const catCount = {};
            manager.animals.forEach(a => {
                catCount[a.category] = (catCount[a.category] || 0) + 1;
            });
            Object.entries(catCount).sort().forEach(([cat, count]) => {
                console.log(`  ${cat}: ${count} 种`);
            });
            console.log('\n');
            break;

        case '--export':
            manager.generateExport();
            break;

        case '--add-animal':
            const readline = require('readline');
            const rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            });
            await manager.handleAddCommand(rl);
            break;

        case '--import-csv':
            if (param) {
                await manager.importFromCsv(param);
            } else {
                console.error('❌ 错误：需要提供 CSV 文件路径');
                console.error('   用法：node manage_animals.js --import-csv <csv文件路径>');
            }
            break;

        case '--generate-sample':
            const count = parseInt(param) || 1000;
            const samples = manager.bulkGenerateSampleAnimals(count);
            manager.bulkAdd(samples);
            manager.saveAnimals();
            console.log(`✓ 已生成并添加 ${count} 种样本动物到 animals_data.json`);
            break;

        default:
            console.log(`❌ 未知命令：${command}`);
            showHelp();
            break;
    }
}

function showHelp() {
    console.log(`
🦁 动物数据管理工具

用法：node manage_animals.js [命令] [参数]

命令列表：
  --stats              查看统计数据
  --export             导出数据到 JSON 文件
  --add-animal         交互式添加新动物
  --import-csv <file>  从 CSV 文件批量导入动物数据
  --generate-sample <N> 生成 N 种样本动物（用于测试）

常用示例：
  node manage_animals.js --stats          # 查看当前数据状态
  node manage_animals.js --export         # 导出数据文件
  node manage_animals.js --add-animal     # 添加单个动物
  node manage_animals.js --import-csv animals_import.csv  # 从 CSV 导入
  node manage_animals.js --generate-sample 1000  # 生成1000种样本动物

要扩展到 1000 种动物，建议：
1. 使用提供的 CSV 模板（animals_import_template.csv）填写所有动物数据
2. 运行：node manage_animals.js --import-csv animals_import.csv
3. 程序将自动导入并保存所有数据

注意：CSV 文件必须包含正确的表头和数据格式，请参考模板文件。
`);
}

// 如果直接运行脚本
if (require.main === module) {
    main().catch(err => {
        console.error('❌ 程序运行出错:', err);
        process.exit(1);
    });
}

module.exports = AnimalDataManager;