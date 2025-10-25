<template>
  <div class="section-card">
    <div class="section-title">📂 选择分析报告</div>
    <div v-if="files.length === 0" style="color: #718096;">
      暂无分析报告
    </div>
    <div v-else class="file-list">
      <button
        v-for="file in displayedFiles"
        :key="file"
        class="file-button"
        :class="{ active: file === currentFile }"
        @click="$emit('select-file', file)"
      >
        {{ file }}
      </button>

      <!-- 折叠/展开按钮 -->
      <button
        v-if="files.length > 6"
        class="file-button"
        style="background: #e2e8f0; color: #2d3748;"
        @click="toggleExpand"
      >
        {{ expanded ? '收起' : '展开更多' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
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

const expanded = ref(false)

const displayedFiles = computed(() => {
  if (expanded.value) return props.files
  return props.files.slice(0, 6)
})

const toggleExpand = () => {
  expanded.value = !expanded.value
}
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
