<template>
  <div class="container">
    <FileSelector
      :files="availableFiles"
      :current-file="currentFile"
      @select-file="loadData"
    />

    <div v-if="loading" class="loading">⏳ 加载中...</div>

    <div v-else-if="error" class="error">
      <h2>❌ 加载失败</h2>
      <p>{{ error }}</p>
    </div>

    <div v-else-if="data">
      <div class="section-card">
        <h1 style="color: #2d3748; font-size: 2.5em; margin-bottom: 10px; display: flex; align-items: center; gap: 15px;">
          🔥 网络热搜趋势分析
        </h1>
        <div style="color: #718096; font-size: 0.9em; margin-top: 10px;">
          📅 更新时间：{{ data.timestamp }}
          <br />
          使用模型：<strong>{{ data.model_used || '未知模型' }}</strong>
        </div>
        <StatsCard :platform-count="platformCount" :total-topics="totalTopics" />
      </div>

      <AnalysisSection :analysis="data.analysis" />

      <div class="section-card">
        <div class="section-title">📱 各平台热搜详情</div>
        
        <!-- 添加平台筛选标签 -->
        <div class="platform-filter">
          <button 
            v-for="category in platformCategories" 
            :key="category.name"
            :class="['filter-btn', { active: activeCategory === category.name }]"
            @click="activeCategory = category.name"
          >
            {{ category.icon }} {{ category.label }}
          </button>
        </div>

        <div class="platforms-grid">
          <PlatformCard
            v-for="[platform, topics] in filteredPlatforms"
            :key="platform"
            :platform="platform"
            :topics="topics"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import FileSelector from './components/FileSelector.vue'
import StatsCard from './components/StatsCard.vue'
import AnalysisSection from './components/AnalysisSection.vue'
import PlatformCard from './components/PlatformCard.vue'

const availableFiles = ref([])
const currentFile = ref(null)
const data = ref(null)
const loading = ref(true)
const error = ref(null)
const activeCategory = ref('all')

// 平台分类
const platformCategories = [
  { name: 'all', label: '全部', icon: '🌐' },
  { name: 'social', label: '社交媒体', icon: '💬', platforms: ['weibo', 'douyin', 'kuaishou'] },
  { name: 'tech', label: '科技资讯', icon: '💻', platforms: ['github', 'v2ex', 'juejin', 'csdn', 'ithome', 'linuxdo', 'nodeseek', 'hostloc'] },
  { name: 'news', label: '新闻媒体', icon: '📰', platforms: ['baidu', 'toutiao', 'thepaper', 'netease-news', 'qq-news', 'sina-news'] },
  { name: 'community', label: '社区论坛', icon: '🗣️', platforms: ['zhihu', 'tieba', 'douban-group', 'newsmth', 'ngabbs', 'hupu'] },
  { name: 'entertainment', label: '娱乐休闲', icon: '🎮', platforms: ['bilibili', 'acfun', 'douban-movie', 'genshin', 'honkai', 'starrail', 'lol', 'miyoushe'] },
]

const platformCount = computed(() => {
  return data.value ? Object.keys(data.value.raw_data).length : 0
})

const totalTopics = computed(() => {
  if (!data.value) return 0
  return Object.values(data.value.raw_data).reduce((sum, topics) => sum + topics.length, 0)
})

// 根据选中的分类过滤平台
const filteredPlatforms = computed(() => {
  if (!data.value) return []
  
  const entries = Object.entries(data.value.raw_data)
  
  if (activeCategory.value === 'all') {
    return entries
  }
  
  const category = platformCategories.find(c => c.name === activeCategory.value)
  if (!category || !category.platforms) {
    return entries
  }
  
  return entries.filter(([platform]) => category.platforms.includes(platform))
})

async function loadFileList() {
  try {
    const response = await fetch('/api/files')
    availableFiles.value = await response.json()

    if (availableFiles.value.length > 0) {
      await loadData(availableFiles.value[0])
    } else {
      loading.value = false
    }
  } catch (err) {
    error.value = '加载文件列表失败'
    loading.value = false
  }
}

async function loadData(filename) {
  try {
    loading.value = true
    error.value = null
    currentFile.value = filename

    const response = await fetch(`/api/data/${filename}`)
    data.value = await response.json()
    loading.value = false
  } catch (err) {
    error.value = '无法加载数据文件，请检查文件是否存在'
    loading.value = false
  }
}

onMounted(() => {
  loadFileList()
})
</script>

<style scoped>
.platforms-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.platform-filter {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 15px;
}

.filter-btn {
  background: white;
  color: #667eea;
  border: 2px solid #667eea;
  padding: 8px 16px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 0.9em;
  transition: all 0.2s;
}

.filter-btn:hover {
  background: #f7fafc;
}

.filter-btn.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: transparent;
}

@media (max-width: 768px) {
  .platforms-grid {
    grid-template-columns: 1fr;
  }
}
</style>