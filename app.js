class AnimalApp {
    constructor() {
        this.animals = [];
        this.categories = new Set();
        this.favorites = new Set();
        this.searchText = '';
        this.selectedCategory = '';
        this.init();
    }

    async init() {
        this.loadAnimalsData();
        this.setupEventListeners();
        this.renderFilters();
        this.renderAnimals();
        this.updateStats();
    }

    loadAnimalsData() {
        // 从内嵌数据加载(300种)
        if (typeof ANIMALS_DATA !== 'undefined' && ANIMALS_DATA.animals && ANIMALS_DATA.animals.length > 0) {
            this.animals = ANIMALS_DATA.animals;
        } else {
            // 兜底:localStorage 旧数据
            const savedData = this.loadFromLocalStorage();
            if (savedData && savedData.animals && savedData.animals.length > 0) {
                this.animals = savedData.animals;
            } else {
                this.animals = this.getSampleAnimals();
            }
        }
        this.animals.forEach(a => this.categories.add(a.category));
        // 收藏只存 id 列表,不覆盖数据
        const savedData = this.loadFromLocalStorage();
        if (savedData && savedData.favorites) {
            this.favorites = new Set(savedData.favorites);
        }
        console.log(`已加载 ${this.animals.length} 种动物数据`);
    }

    saveFavorites() {
        try {
            localStorage.setItem('animalIntroFavorites', JSON.stringify(Array.from(this.favorites)));
            return true;
        } catch (e) {
            console.warn('无法保存收藏:', e);
            return false;
        }
    }

    loadFromLocalStorage() {
        try {
            const fav = localStorage.getItem('animalIntroFavorites');
            return fav ? { favorites: JSON.parse(fav) } : null;
        } catch (e) {
            return null;
        }
    }

    getSampleAnimals() {
        return [
            {id:1,name:'大熊猫',category:'哺乳类',scientificName:'Ailuropoda melanoleuca',habitat:'中国四川、陕西、甘肃山区竹林',diet:'主要以竹子为食（99%），偶尔吃小型动物和鸟类',size:'体长60-85cm，体重15-125kg',weight:'100kg',length:'0.7m',status:'易危(VU)',image:'images/giant-panda.jpg',emoji:'🐼',description:'中国的国宝，黑白相间，以竹子为主食，憨态可掬。'},
            {id:2,name:'金丝猴',category:'哺乳类',scientificName:'Rhinopithecus roxellana',habitat:'中国西南和中部的高山森林（海拔2200-3400米）',diet:'水果、树叶、种子、树皮和昆虫',size:'体长约75cm，尾巴与身长相等',weight:'10-15kg',length:'0.75m',status:'濒危(EN)',image:'images/golden-snub-nosed-monkey.jpg',emoji:'🙎',description:'毛发金黄如丝，面部蓝色，是中国特有的珍稀灵长类动物。'}
        ];
    }

    renderFilters() {
        const filterContainer = document.getElementById('categoryFilters');
        const categorySelect = document.getElementById('categoryFilter');

        const sortedCategories = Array.from(this.categories).sort();
        filterContainer.innerHTML = '';

        sortedCategories.forEach(category => {
            const btn = document.createElement('button');
            btn.className = 'filter-btn';
            btn.textContent = category;
            btn.onclick = () => this.filterByCategory(category);
            filterContainer.appendChild(btn);
        });

        const allBtn = document.createElement('button');
        allBtn.className = 'filter-btn active';
        allBtn.textContent = '全部';
        allBtn.onclick = () => this.showAllCategories();
        filterContainer.insertBefore(allBtn, filterContainer.firstChild);

        const categorySelectElement = document.getElementById('categoryFilter');
        categorySelectElement.innerHTML = '<option value="">全部类别</option>';
        sortedCategories.forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            option.textContent = category;
            categorySelectElement.appendChild(option);
        });
    }

    filterByCategory(category) {
        this.selectedCategory = category;
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        this.renderAnimals();
    }

    showAllCategories() {
        this.selectedCategory = '';
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        const allBtn = document.querySelector('.filter-btn:first-child');
        if (allBtn) allBtn.classList.add('active');
        this.renderAnimals();
    }

    renderAnimals() {
        let filtered = this.animals;
        if (this.selectedCategory) {
            filtered = filtered.filter(a => a.category === this.selectedCategory);
        }
        if (this.searchText) {
            const t = this.searchText.toLowerCase();
            filtered = filtered.filter(a =>
                (a.name && a.name.toLowerCase().includes(t)) ||
                (a.scientificName && a.scientificName.toLowerCase().includes(t)) ||
                (a.englishName && a.englishName.toLowerCase().includes(t)) ||
                (a.description && a.description.includes(this.searchText))
            );
        }

        const grid = document.getElementById('animalsGrid');
        grid.innerHTML = '';

        if (filtered.length === 0) {
            grid.innerHTML = '<div class="no-results"><h3>未找到匹配的动物</h3><p>试试调整搜索或筛选条件。</p></div>';
            return;
        }

        filtered.forEach(animal => {
            const isFavorite = this.favorites.has(animal.id);
            const card = document.createElement('div');
            card.className = 'animal-card';
            card.innerHTML = `
                <div class="animal-header">
                    <div class="animal-avatar">${animal.emoji}</div>
                    <img src="${animal.image}" alt="${animal.name}" loading="lazy" class="animal-image" onerror="this.outerHTML='<div class=animal-image-broken>'+this.alt+'</div>'">
                </div>
                <div class="animal-info">
                    <div class="animal-name">${animal.name}</div>
                    <span class="animal-category">${animal.category}</span>
                    <div class="animal-scientific">${animal.scientificName}</div>
                    <div class="animal-stats">
                        <div class="stat-item">⚖️ ${animal.weight}</div>
                        <div class="stat-item">📏 ${animal.length}</div>
                        <div class="stat-item">🔴 ${animal.status}</div>
                    </div>
                    <div class="animal-desc">${animal.description}</div>
                    <div class="animal-actions">
                        <button class="action-btn btn-favorite ${isFavorite ? 'favorite-active' : ''}" onclick="app.toggleFavorite(${animal.id})">${isFavorite ? '❤️ 取消收藏' : '⭐ 收藏'}</button>
                        <button class="action-btn btn-detail" onclick="app.showDetail(${animal.id})">详情</button>
                    </div>
                </div>
            `;
            grid.appendChild(card);
        });
    }

    toggleFavorite(id) {
        if (this.favorites.has(id)) {
            this.favorites.delete(id);
        } else {
            this.favorites.add(id);
        }
        this.saveFavorites();
        this.updateStats();
        this.renderAnimals();
    }

    showDetail(id) {
        const animal = this.animals.find(a => a.id === id);
        if (!animal) return;
        const habitat = animal.habitat || '未知';
        const diet = animal.diet || '未知';
        const size = animal.size || '未知';
        const detail = `${animal.name}（${animal.scientificName}）\n\n分类：${animal.category}\n栖息地：${habitat}\n食性：${diet}\n体型：${size}\n重量：${animal.weight || '未知'}\n长度：${animal.length || '未知'}\n保护级别：${animal.status}\n\n${animal.description}`;
        alert(detail);
    }

    updateStats() {
        document.getElementById('totalAnimals').textContent = this.animals.length;
        document.getElementById('categoriesCount').textContent = this.categories.size;
        document.getElementById('favoritesCount').textContent = this.favorites.size;

        let totalLength = 0, count = 0;
        this.animals.forEach(a => {
            if (a.length) {
                const match = String(a.length).match(/[\d.]+/);
                if (match) {
                    const l = parseFloat(match[0]);
                    if (!isNaN(l) && l < 100) { totalLength += l; count++; }
                }
            }
        });
        const avg = count > 0 ? (totalLength / count).toFixed(2) : '-';
        document.getElementById('avgSize').textContent = avg;
    }

    setupEventListeners() {
        const searchBox = document.getElementById('searchBox');
        searchBox.addEventListener('input', (e) => {
            this.searchText = e.target.value;
            this.renderAnimals();
        });

        const categoryFilter = document.getElementById('categoryFilter');
        categoryFilter.addEventListener('change', (e) => {
            this.selectedCategory = e.target.value;
            this.renderAnimals();
            this.filterByCategory(e.target.value);
        });
    }
}

let app;
document.addEventListener('DOMContentLoaded', () => {
    app = new AnimalApp();
});

window.app = app;
window.toggleFavorite = function(id) { app.toggleFavorite(id); };
window.showDetail = function(name) { app.showDetail(name); };
