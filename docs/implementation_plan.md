# 実装計画書 (Implementation Plan) - 活動実績HP

## 概要
iU情報経営イノベーション専門職大学 客員教授（Sho T氏）の活動実績を公開するポートフォリオサイトを構築します。
更新性と運用コストを考慮し、**Astro** を使用した静的サイトとし、**GitHub Pages** で公開します。

## ユーザーレビューが必要な事項
- デザイン: Vanilla CSSを用いたシンプルかつプレミアムなデザイン（テンプレートは使用せず独自実装）。
- 画像素材: `/public/images/` フォルダへの画像配置が必要になります。

## 技術スタック
- **Framework**: Astro (推奨) - 高速、シンプル、Content Collections機能が強力。
- **Styling**: Vanilla CSS (Scoped CSS) - 柔軟性と将来的な保守性を重視。
- **Hosting**: GitHub Pages
- **CI/CD**: GitHub Actions

## ディレクトリ構成
```text
/
├── public/
│   └── images/          # 画像アセット（年度別フォルダ分け推奨: 2024/, 2025/ 等）
├── src/
│   ├── components/      # UIコンポーネント
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── Hero.astro
│   │   ├── ActivityList.astro
│   │   └── Gallery.astro
│   ├── layouts/         # ページレイアウト
│   │   └── Layout.astro # 共通レイアウト
│   ├── pages/           # ページルーティング
│   │   └── index.astro  # トップページ（全コンテンツを集約）
│   ├── content/
│   │   └── activities/  # 活動実績データ (Markdown)
│   │       ├── profile.md # プロフィール情報
│   │       ├── 2025.md
│   │       ├── 2024.md
│   │       └── ...
│   └── styles/
│       └── global.css   # グローバルスタイル（変数、リセット等）
├── astro.config.mjs     # Astro設定
└── package.json
```

## 実装ステップ

### 1. プロジェクト初期化
- Astroプロジェクトの作成 (`npm create astro@latest`)
- 必要な依存関係のインストール

### 2. 基盤実装
- Global CSSの設定 (Color Palette, Typography)
- Layoutコンポーネントの実装 (SEO metaタグ含む)
- Header / Footerの実装

### 3. データ構造の定義
- Content Collectionsの設定 (`src/content/config.ts`)
- スキーマ定義 (year, summary, galleryImages[], detailsBody)
- **※初期実装方針**: 「年単位」のMarkdownファイル(`2025.md`等)で管理します。「記事単位（1件ごと）」の追加は将来的な拡張機能としてデータ構造のみ考慮しておきます。

### 4. コンポーネント実装
- **Hero**: プロフィールとメインビジュアル
- **ActivitySection**: 年ごとのセクション表示
- **Gallery**: 無限スクロール（Marquee）アニメーションによる画像表示
    - 画像数に応じて1〜3行に自動分割
    - CSSアニメーションによるスムーズなスクロール
- **Timeline**: 時系列表示の制御

### 5. コンテンツ流し込み
- 頂いた仕様書のテキストデータをMarkdown化して配置
- 画像フォルダ(`public/images/`)の日本語ディレクトリ名をWeb標準(英数)に変更することを推奨・実施
- `.env` や機密情報が含まれないことを確認

### 6. デプロイ設定
- GitHub Actionsワークフローの作成 (`.github/workflows/deploy.yml`)
- GitHub Pages用のビルド設定

### 7. 便利ツール (Utility)
- **[NEW] PreviewWebsite.command**: ダブルクリックするだけでローカルサーバー(`npm run dev`)を起動するMac用実行ファイル。

## 検証計画
### 自動ビルドチェック
- `npm run build` がエラーなく完了すること。

### UI確認
- レスポンシブ確認（スマホ/PC）
- 画像ギャラリーのレイアウト崩れがないか
- リンク（SNS等）の動作確認
