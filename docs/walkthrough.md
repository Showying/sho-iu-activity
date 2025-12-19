# 開発手順書 (Walkthrough) - 活動実績HP

## 実施した変更

### 1. プロジェクト基盤構築
- Astroプロジェクトのセットアップ（`npm create astro -- minimal`）。
- グローバルCSS (`src/styles/global.css`) の作成。シンプルでプレミアム感のあるデザインシステムを定義。
- レイアウトコンポーネント (`src/layouts/Layout.astro`) の実装。

### 2. コンテンツ移行
- 提供された活動実績テキスト全量（2025年〜2021年）を `src/content/activities/` にMarkdown形式で配置。
- プロフィール情報を `src/content/profile/main.md` に配置。
- 画像フォルダ (`public/images/`) を整理し、日本語フォルダ名を英数字にリネーム（Web表示対策）。

### 3. コンポーネント実装
- **Header/Footer**: シンプルでオフィシャル感のあるナビゲーションとフッター。
- **Hero**: プロフィール情報を美しく表示するメインビジュアル。
- **Gallery**: 各年の画像フォルダから自動的に画像を読み込んで一覧表示するロジックを実装。
- **ActivityList**: 活動実績のタイムライン表示と、Galleryの統合。

### 4. デプロイ設定
- GitHub Actionsワークフロー (`.github/workflows/deploy.yml`) を作成。
- 運用マニュアル (`README.md`) を作成。

## 検証結果

### 自動テスト
- [x] `npm run build` がエラーなく完了し、静的ファイルが生成されることを確認しました。

### 機能確認（コードベース）
- [x] コンテンツコレクションのスキーマ定義が正しく機能していること。
- [x] ギャラリー画像のパス解決が正常に行われるロジックであること（fsモジュール使用）。

## 次のステップ（ユーザー作業）
1. GitHub Desktopで変更をコミット＆プッシュする。
2. GitHubのリポジトリ設定で、PagesのSourceを「GitHub Actions」に変更する。
3. 公開URLを確認する。
