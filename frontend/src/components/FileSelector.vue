<template>
  <div class="section-card">
    <div class="section-title">📂 选择分析报告</div>
    <div v-if="files.length === 0" style="color: #718096;">
      暂无分析报告
    </div>
    <div v-else class="file-list">
      <button
        v-for="file in files"
        :key="file"
        class="file-button"
        :class="{ active: file === currentFile }"
        @click="$emit('select-file', file)"
      >
        {{ file }}
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  files: {
    type: Array,
    required: true
  },
  currentFile: {
    type: String,
    default: null
  }
})

defineEmits(['select-file'])
</script>

<style scoped>
.file-list {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 15px;
}

.file-button {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.95em;
  transition: transform 0.2s, box-shadow 0.2s;
}

.file-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.file-button.active {
  background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
}
</style>