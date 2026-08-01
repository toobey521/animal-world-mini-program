// animal-images-generator.js
/**
 * 动物图片生成脚本框架
 * 此文件需要配合 agnes-image API 使用
 *
 * 使用说明：
 * 1. 首先需要获得 agnes-image API 的访问权限和密钥
 * 2. 在此文件中配置API参数
 * 3. 运行此脚本批量生成卡通动物图片
 */

const fs = require('fs');
const axios = require('axios'); // 需要 npm install axios

class ImageGenerator {
    constructor(apiKey, version = 'agnes-image-2.0-flash') {
        this.apiKey = apiKey;
        this.version = version;
        this.apiUrl = `https://api.agnes.com/v/${version}/generate`;
        this.animalsFile = 'animals_data.json';
    }

    async generateAnimalImages(animalList) {
        const results = [];

        for (const animal of animalList) {
            try {
                const prompt = `卡通风格，可爱${animal.name}，白色背景，矢量插画，简洁明亮，适合儿童教育应用`;

                const response = await axios.post(this.apiUrl, {
                    prompt: prompt,
                    size: '512x512',
                    style: 'cartoon',
                    count: 1
                }, {
                    headers: {
                        'Authorization': `Bearer ${this.apiKey}`,
                        'Content-Type': 'application/json'
                    }
                });

                // 保存图片（实际需要根据API返回处理）
                const imageUrl = response.data.url; // 根据实际API结构调整
                await this.saveImage(imageUrl, animal.imagePlaceholder || `${animal.name}.jpg`);

                results.push({
                    name: animal.name,
                    success: true,
                    imageFile: animal.imagePlaceholder || `${animal.name}.jpg`
                });

                console.log(`✓ 已生成：${animal.name} (${animal.imagePlaceholder || animal.name + '.jpg'})`);

                // 避免过快调用API
                await this.delay(1000);

            } catch (error) {
                results.push({
                    name: animal.name,
                    success: false,
                    error: error.message
                });
                console.error(`✗ 失败：${animal.name} - ${error.message}`);
            }
        }

        return results;
    }

    async saveImage(url, filename) {
        // 下载图片并保存到本地目录
        // 这里只是示例，实际需要根据下载逻辑实现
        console.log(`⬇️ 图片下载到：${filename}`);
        // 实际需要实现图片下载保存逻辑
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async processAllAnimals() {
        // 加载动物数据
        let animals;
        if (fs.existsSync(this.animalsFile)) {
            animals = JSON.parse(fs.readFileSync(this.animalsFile, 'utf8'));
        } else {
            // 使用内置的默认动物列表
            animals = this.getDefaultAnimaless();
        }

        // 生成所有图片
        console.log(`开始为 ${animals.length} 种动物生成卡通图片...`);
        const results = await this.generateAnimalImages(animals);

        // 保存结果日志
        fs.writeFileSync('image_generation_log.json', JSON.stringify(results, null, 2), 'utf8');
        console.log(`\n完成！成功：${results.filter(r => r.success).length} / 总：${results.length}`);

        return results;
    }

    getDefaultAnimaless() {
        return [
            { name: '大熊猫', imagePlaceholder: 'panda.jpg' },
            { name: '金丝猴', imagePlaceholder: 'goldenmonkey.jpg' },
            { name: '藏羚羊', imagePlaceholder: 'tibetan_antelope.jpg' },
            { name: '朱鹮', imagePlaceholder: 'nisin.jpg' },
            { name: '白鱀豚', imagePlaceholder: 'baiji_dolphin.jpg' }
            // ... 这里可以添加更多直到1000种
        ];
    }
}

// 从环境变量或配置文件读取API密钥
const API_KEY = process.env.AGNES_IMAGE_API_KEY || 'your-api-key-here';

if (API_KEY === 'your-api-key-here') {
    console.error('错误：请先设置 AGNES_IMAGE_API_KEY 环境变量或修改此文件中的API密钥');
    process.exit(1);
}

// 初始化并执行
const generator = new ImageGenerator(API_KEY);
generator.processAllAnimals().catch(console.error);

module.exports = ImageGenerator;