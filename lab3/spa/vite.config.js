import path from 'path';
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      'vue': 'vue/dist/vue.esm-bundler.js',
    },
    extensions: ['.js', '.json', '.ts', '.vue', '.jsx']
  },
  proxy: {
    '/api': {
      target: 'https://localhost:8000',
      changeOrigin: true,
      secure: false,
      ws: true
    }
  }
});