<template>
  <div class="platform-card">
    <div class="platform-name">
      <span class="platform-icon">{{ platformIcon }}</span>
      <span>{{ displayName }}</span>
    </div>
    <ul class="topic-list">
      <li v-for="(topic, index) in topics" :key="index" class="topic-item">
        <span class="topic-number">{{ index + 1 }}</span>
        <span class="topic-text">{{ topic }}</span>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { getPlatformName } from '../config/platforms'

const props = defineProps({
  platform: {
    type: String,
    required: true
  },
  topics: {
    type: Array,
    required: true
  }
})

// 获取平台中文名称
const displayName = computed(() => getPlatformName(props.platform))

// 为所有平台配置图标
const platformIcon = computed(() => {
  const iconMap = {
    'weibo': '🔴',           // 微博 
    'zhihu': '🔵',           // 知乎 
    'zhihu-daily': '📘',     // 知乎日报 
    'baidu': '🔍',           // 百度 
    'toutiao': '📰',         // 今日头条 
    'qq-news': '🐧',         // 腾讯新闻 
    'sina-news': '📡',       // 新浪新闻 
    'sina': '🌊',            // 新浪 
    'netease-news': '📬',    // 网易新闻 
    'thepaper': '📄',        // 澎湃新闻 
    'douyin': '🎵',          // 抖音 
    'kuaishou': '⚡',        // 快手 
    'bilibili': '📺',        // 哔哩哔哩 
    'acfun': '🅰️',          // AcFun 
    'douban-movie': '🎬',    // 豆瓣电影 
    'douban-group': '👥',    // 豆瓣小组 
    'weread': '📚',          // 微信读书 
    'github': '💻',          // GitHub 
    'juejin': '⛏️',         // 稀土掘金 
    'csdn': '💾',            // CSDN 
    'v2ex': '🛠️',           // V2EX 
    'ithome': '🏠',          // IT之家 
    'ithome-xijiayi': '🎁',  // IT之家喜加一 
    'linuxdo': '🐧',         // LinuxDo 
    'nodeseek': '🔌',        // NodeSeek 
    'hostloc': '🖥️',        // HostLoc 
    '51cto': '🎓',           // 51CTO 
    'hellogithub': '👋',     // HelloGitHub 
    'tieba': '💬',           // 百度贴吧 
    'newsmth': '🌲',         // 水木社区 
    'ngabbs': '🎮',          // NGA 
    'hupu': '🏀',            // 虎扑 
    'coolapk': '📱',         // 酷安 
    '36kr': '💼',            // 36氪 
    'huxiu': '🐯',           // 虎嗅 
    'geekpark': '🚀',        // 极客公园 
    'ifanr': '🍎',           // 爱范儿 
    'smzdm': '💰',           // 什么值得买 
    'sspai': '⚙️',           // 少数派 
    'producthunt': '🎯',     // Product Hunt 
    'genshin': '⚔️',         // 原神 
    'honkai': '⚡',          // 崩坏3 
    'starrail': '🚂',        // 崩坏星穹铁道 
    'miyoushe': '🎮',        // 米游社 
    'lol': '🏆',             // 英雄联盟 
    'gameres': '🎲',         // 游资网 
    'yystv': '🎪',           // 游研社 
    'dgtle': '📐',           // 数字尾巴 
    'jianshu': '✍️',         // 简书 
    'guokr': '🔬',           // 果壳 
    'earthquake': '🌋',      // 地震速报 
    'weatheralarm': '⚠️',    // 天气预警 
    'history': '📅',         // 历史上的今天 
    'hackernews': '🟠',      // Hacker News 
    'nytimes': '📰',         // 纽约时报 
    '52pojie': '🔓',         // 吾爱破解 
  }
  
  return iconMap[props.platform] || '🌐'  // 默认使用地球图标
})
</script>

<style scoped>
.platform-card {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.platform-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
}

.platform-name {
  font-weight: bold;
  color: #667eea;
  font-size: 1.2em;
  margin-bottom: 15px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.platform-icon {
  font-size: 1.3em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 28px;
}

.topic-list {
  list-style: none;
}

.topic-item {
  padding: 12px;
  color: #4a5568;
  border-bottom: 1px solid #e2e8f0;
  font-size: 0.95em;
  height: 48px;
  display: flex;
  align-items: center;
  transition: all 0.3s ease;
  position: relative;
  cursor: pointer;
  border-radius: 8px;
  margin-bottom: 4px;
}

.topic-item:last-child {
  border-bottom: none;
}

.topic-item:hover {
  background: #f7fafc;
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  z-index: 10;
  height: auto;
  min-height: 48px;
}

.topic-text {
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.topic-item:hover .topic-text {
  white-space: normal;
  word-wrap: break-word;
}

.topic-number {
  display: inline-block;
  background: #667eea;
  color: white;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  text-align: center;
  line-height: 24px;
  font-size: 0.85em;
  margin-right: 10px;
  flex-shrink: 0;
}
</style>