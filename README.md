# Sho T Activity Portfolio

iU情報経営イノベーション専門職大学 客員教授 Sho T（高橋 翔）の活動実績ポートフォリオサイトです。
Astroで構築され、GitHub Pagesでホスティングされます。

## 🚀 プロジェクト概要
- **URL**: (GitHub PagesのURL、設定完了後に反映されます)
- **Framework**: [Astro](https://astro.build)
- **Styling**: Vanilla CSS (Scoped)

## 📝 運用・更新マニュアル

### 1. 新しい活動実績（年）を追加する
1. `src/content/activities/` 内に新しいMarkdownファイルを作成します（例: `2026.md`）。
2. 以下のフォーマットで記述してください。
```markdown
---
year: 2026
summary: "その年の活動サマリーを記述..."
galleryImages: []
---
(ここに詳細な実績リストを記述)
```

### 2. 画像を追加する
1. `public/images/{年}/` フォルダを作成または開きます（例: `public/images/2026/`）。
2. 画像ファイル（jpg, png等）を配置します。
3. サイト上のギャラリーに自動的に反映されます。

### 3. プロフィールを更新する
1. `src/content/profile/main.md` を編集してください。

## 💻 ローカルでの開発

### 方法1: ターミナルから起動（推奨）
```bash
# 依存関係のインストール
npm install

# 開発サーバーの起動 (localhost:4321)
npm run dev
```

### 方法2: Mac Appletから起動（ワンクリック）
プロジェクトフォルダ内の `sho-iu-activity.app` をダブルクリックしてください。
ターミナルが立ち上がり、自動的にブラウザが開きます。

> **Note: アイコンの設定方法**
> 1. `public/app-icon.png` をプレビュー.appで開く。
> 2. `Cmd + A` (全選択) -> `Cmd + C` (コピー)。
> 3. `sho-iu-activity.app` を右クリック -> 「情報を見る」。
> 4. 左上のアイコン画像をクリックして選択状態にする。
> 5. `Cmd + V` (貼り付け)。

# ビルドチェック
npm run build


## 🌍 公開手順
`main` ブランチにプッシュすると、GitHub Actionsが自動的にビルドし、GitHub Pagesへデプロイします。

**初回設定:**
1. GitHubリポジトリの **Settings > Pages** を開く。
2. **Build and deployment > Source** で **GitHub Actions** を選択する。
