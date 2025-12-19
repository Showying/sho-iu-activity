// @ts-check
import { defineConfig } from 'astro/config';

// npm run build (GitHub Actions等) の時はサブディレクトリを適用
// npm run dev (ローカル) の時はルートパスを使用
const isBuild = process.argv.includes('build');

// https://astro.build/config
export default defineConfig({
    site: 'https://Showying.github.io',
    base: isBuild ? '/sho-iu-activity' : '/',
});
