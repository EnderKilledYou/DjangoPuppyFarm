import {fileURLToPath, URL} from 'node:url'
import path from "path";
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'


// https://vitejs.dev/config/
export default defineConfig({
    build: {
        outDir: path.resolve(__dirname, "../app/vue"),
        emptyOutDir: true
    },
    plugins: [vue(), vueJsx()],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    }
})
