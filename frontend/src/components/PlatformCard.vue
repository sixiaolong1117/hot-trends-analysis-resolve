<template>
  <div class="platform-card">
    <div class="platform-name">🌐 {{ platform }}</div>
    <ul class="topic-list">
      <li v-for="(topic, index) in topics" :key="index" class="topic-item">
        <span class="topic-number">{{ index + 1 }}</span>
        <span class="topic-text">{{ topic }}</span>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  platform: {
    type: String,
    required: true
  },
  topics: {
    type: Array,
    required: true
  }
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