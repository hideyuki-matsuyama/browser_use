# 🚧WIP

- AI エージェントがウェブブラウザを操作できるようにするためのライブラリ [Browser Use](https://github.com/browser-use/browser-use) を利用して、検索キーワードに該当する WEB サイトの URL を収集するプログラムです
- OpenAI が提供するライブラリ `ChatOpenAI` を用いて、指定の AI モデルに指示を与え、結果をテキストファイルに保存します。

# 気付き

- AI モデルごとのプロンプトの癖を判断して振り分ける処理を AI に任せたいという禅問答に突入
- トライ＆エラーの過程を含め学習していてくれるが、実行するたびに結果が異なったりして一貫性に疑念が生じる
  - Gemini 2.5 Pro(preview) にて「実行するたび結果が異なるため、これまでの処理結果を全て破棄してください」が有効だった（2025.05.17 時点）
- 結局 CoT (Chain of Thought)を読んで対応するので、限りなくプログラミングに近い思考が必要
  - 指示がどう解釈・実行されているのか確認するためにも、ユーザーは CoT を読むべき 
  - Gemini 2.5 Pro(preview) にて `Chain of Thought を日本語で出力してください` が有効なのを確認（2025.05.17 時点）
- Gemini に「duckduckgo を使って」とお願いしたが、現在のツールでは検索エンジンが指定不可とのことでダメだった
- 繰り返す処理を指示した際、件数を増やすと 1 件あたりの精度を下げる傾向が見受けられた

# メモ

```sh
python3 -m venv venv
source venv/bin/activate
pip install browser-use

playwright install

rm -rf venv
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install browser-use
pip install python-dotenv
```
