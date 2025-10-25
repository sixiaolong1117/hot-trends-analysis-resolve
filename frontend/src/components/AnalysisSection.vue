<template>
  <div class="section-card">
    <div class="section-title">📊 AI 分析总结</div>
    <div class="analysis-content markdown-body" v-html="renderedMarkdown"></div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { marked } from 'marked'

const props = defineProps({
  analysis: {
    type: String,
    required: true
  }
})

const renderedMarkdown = computed(() => {
  const markdownContent = props.analysis.replace(/\\n/g, '\n')
  return marked.parse(markdownContent)
})
</script>

<style scoped>
.analysis-content {
  color: #4a5568;
  line-height: 1.8;
  font-size: 1.1em;
}

.analysis-content :deep(h1),
.analysis-content :deep(h2),
.analysis-content :deep(h3) {
  margin-top: 1.5em;
  margin-bottom: 0.5em;
  color: #2d3748;
}

.analysis-content :deep(p) {
  margin-bottom: 1em;
}

.analysis-content :deep(ul),
.analysis-content :deep(ol) {
  margin-left: 1.5em;
  margin-bottom: 1em;
}

.analysis-content :deep(code) {
  background: #f7fafc;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: monospace;
}
</style>