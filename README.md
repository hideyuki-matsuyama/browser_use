# 🚧WIP

- AI エージェントがウェブブラウザを操作できるようにするためのライブラリ [Browser Use](https://github.com/browser-use/browser-use) を利用して、検索キーワードに該当する WEB サイトの URL を収集するプログラムです
- OpenAI が提供するライブラリ `ChatOpenAI` を用いて、指定の AI モデルに指示を与え、結果をテキストファイルに保存します。

# 気付き

- AI モデルごとのプロンプトの癖を判断して振り分ける処理を AI に任せたいという禅問答に突入
- トライ＆エラーの過程で自動的に学習していてくれるが、これまでの実行履歴をリセットして実行させたい場合がある
- 結局 Chain of Thought (CoT)を読んで対応するので、限りなくプログラミングに近い思考が必要

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
