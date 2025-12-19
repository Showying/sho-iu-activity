# タスク管理

## 最重要：行動指針 (Behavioral Guidelines)
以下のルールは絶対順守です。

1.  **全てのコメントに回答**: ユーザーのコメントの内容全てに対し、漏れなく回答すること。
2.  **実装前の確認**: 何かを実装する時は必ず、「〜〜を実装して良いですか？なぜならXXXをするためです」と確認をとること。
3.  **コマンド実行の事前説明とターン分割**: `run_command` 等を実行する際は、いきなり実行せず、必ず直前のターンで日本語で内容を説明し、ターンを分けてから実行すること。
4.  **Accept時の事前説明**: コード修正やコマンド実行でユーザーの承認（Accept）が必要な場合は、必ず手前のターンで日本語の説明を行い、説明と実行を分けること。
5.  **完了確認**: 「できた」と言う前に、本当にできているかを確認（検証）した上で、できたと言うこと。
6.  **ドキュメントの同期**: `task.md`, `implementation_plan.md`, `walkthrough.md` は必ず `docs/` フォルダにもコピーを配置し、更新があるたびに自動的に同期（最新化）すること。

## 現在のステータス
- **フェーズ**: デザイン改善 (Design Polish)
- **状態**: デザインロールバック

## TODOリスト

### 0. プロジェクト初期設定（完了）
- [x] ドキュメントフォルダ(`docs`)の作成 <!-- id: 0 -->
- [x] 行動指針(`task.md`)の策定と配置 <!-- id: 1 -->
- [x] `docs`フォルダへのファイル同期 <!-- id: 2 -->
- [/] ユーザーへのGitHub Desktop連携手順の案内 <!-- id: 3 -->
- [x] `.gitignore` の作成（セキュリティ対応） <!-- id: 4 -->
- [x] `.env` ファイルの設計と作成（テンプレート） <!-- id: 5 -->
- [x] 重要なファイルがgitに含まれないよう `.gitignore` 設定 <!-- id: 6 -->
- [x] `implementation_plan.md` (docs/含む) の作成 <!-- id: 7 -->
- [x] `walkthrough.md` (docs/含む) の作成 <!-- id: 8 -->

### 1. Webサイト基盤構築
- [x] Astroプロジェクトの初期化 (npm create astro) <!-- id: 9 -->
- [x] ディレクトリ構成の整備 (src/components, src/content等) <!-- id: 10 -->
- [x] グローバルCSSとデザインシステムの定義 (Colors, Fonts) <!-- id: 11 -->
- [x] 共通レイアウト(Layout.astro), Header, Footerの実装 <!-- id: 12 -->

### 2. メイン機能・コンポーネント実装
- [x] コンテンツスキーマ定義 (Content Collections) <!-- id: 13 -->
- [x] Heroセクション（プロフィール）の実装 <!-- id: 14 -->
- [x] Activityセクション（年別実績）の実装 <!-- id: 15 -->
- [x] Galleryコンポーネント（画像グリッド）の実装 <!-- id: 16 -->
- [x] トップページ(index.astro)への組み込み <!-- id: 17 -->

### 3. コンテンツ移行
- [x] 提供された活動実績テキストのMarkdown化 (2025, 2024...) <!-- id: 18 -->
- [x] 画像アセットの配置案内と確認 <!-- id: 19 -->

### 4. デプロイと公開
- [x] GitHub Actions設定ファイルの作成 (.github/workflows/deploy.yml) <!-- id: 20 -->
- [x] ビルド確認と修正 <!-- id: 21 -->
- [x] 運用マニュアル(README.md)の整備 <!-- id: 22 -->

### 5. 便利ツール (Utility)
- [x] Mac用Applet(sho-iu-activity.app)の作成 <!-- id: 23 -->

### 6. デザイン改善 (Design Polish)
- [ ] Global CSSの刷新 (Typography, Colors, Animations) <!-- id: 24 -->
- [ ] Heroセクションのスタイリッシュ化 <!-- id: 25 -->
- [ ] ActivityTimelineのデザイン刷新 <!-- id: 26 -->
- [ ] Header/Footerのモダン化 (Glassmorphism) <!-- id: 27 -->
