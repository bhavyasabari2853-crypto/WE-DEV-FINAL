import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Configuration for development and GitHub Pages deployment
export default defineConfig({
  plugins: [react()],
  // When serving from GitHub Pages at https://<user>.github.io/WE-DEV-FINAL/
  base: '/WE-DEV-FINAL/',
  build: {
    // Output files into repository root `docs/` folder for GitHub Pages
    outDir: '../docs',
    emptyOutDir: true,
  },
  server: {
    port: 5173,
    host: 'localhost'
  }
})
