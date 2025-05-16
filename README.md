# 🚧WIP

- AI エージェントがウェブブラウザを操作できるようにするためのライブラリ [Browser Use](https://github.com/browser-use/browser-use) を利用して、検索キーワードに該当する WEB サイトの URL を収集するプログラムです
- OpenAI が提供するライブラリ `ChatOpenAI` を用いて、指定の AI モデルに指示を与え、結果をテキストファイルに保存します。

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
