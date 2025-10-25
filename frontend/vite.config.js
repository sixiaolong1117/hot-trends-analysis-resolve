import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: '/',  // 确保资源路径正确
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    // 生成相对路径的资源引用
    rollupOptions: {
      output: {
        manualChunks: undefined
      }
    }
  }
})