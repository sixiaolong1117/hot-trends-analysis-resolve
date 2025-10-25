<template>
  <div class="stats">
    <div class="stat-card">
      <div class="stat-label">分析平台</div>
      <div class="stat-value">{{ platformCount }}</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">热搜条目</div>
      <div class="stat-value">{{ totalTopics }}</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  platformCount: {
    type: Number,
    required: true
  },
  totalTopics: {
    type: Number,
    required: true
  }
})
</script>

<style scoped>
.stats {
  display: flex;
  gap: 20px;
  margin-top: 20px;
  flex-wrap: wrap;
}

.stat-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 15px 25px;
  border-radius: 12px;
  flex: 1;
  min-width: 150px;
}

.stat-label {
  font-size: 0.85em;
  opacity: 0.9;
}

.stat-value {
  font-size: 2em;
  font-weight: bold;
  margin-top: 5px;
}

@media (max-width: 768px) {
  .stats {
    flex-direction: column;
  }
}
</style>