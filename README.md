[![Pylint](https://github.com/hideyuki-matsuyama/browser_use/actions/workflows/pylint.yml/badge.svg)](https://github.com/hideyuki-matsuyama/browser_use/actions/workflows/pylint.yml)

# 🚧WIP

- AI エージェントがウェブブラウザを操作できるようにするためのライブラリ [Browser Use](https://github.com/browser-use/browser-use) を利用して、検索キーワードに該当する WEB サイトの URL を収集するプログラムです
- OpenAI が提供するライブラリ `ChatOpenAI` を用いて、指定の AI モデルに指示を与え、結果をテキストファイルに保存します。

# 気付き

```md
あなたは URL 調査を担当するエージェントで、検索キーワードに該当する公式ページの URL を収集します。

<!-- - Chain of Thought を日本語で出力してください -->

- 実行するたび結果が異なるため、これまでの処理結果を全て破棄してください
- 実行するたび結果が異なるため、シークレットモードで実行してください
- 与えられた検索キーワードで以下をループしてください:
  - 検索キーワードで検索してください
  - 見つからなかった場合の文言を一律 `URLなし` としてください
  - 検索結果の上から順に以下をループしてください:
    - 以下に該当するページを除外するようフィルタリングしてください:
      - 除外サイト_A
      - 除外サイト_B
      - 除外サイト_C
    - ナレッジパネルがあればウェブサイトの URL を取得してください
    - 検索キーワードから推測した公式ページを取得してください:
      - 見つからなかった場合はフィルタリング後リストの最初の 1 件を取得してください
  - 公式ページが見つかっている場合はトップページの URL を返してください

結果を以下の様式で、見つかったかどうかの結果を問わず全件を返してください。その際、markdown 記法に加工しないでください:
<検索キーワード> <公式ページの URL> <公式ページのタイトル>

以下の検索キーワードを使用してください:
キーワード_1
キーワード_2
キーワード_3
```

- AI モデルごとのプロンプトの癖を判断して振り分ける処理を AI に任せたいという禅問答に突入しかけた
- トライ＆エラーの過程で学習してくれるが、実行するたびに結果が異なることが多く一貫性が無さそうに見えた
  - Gemini 2.5 Pro(preview) にて「実行するたび結果が異なるため、これまでの処理結果を全て破棄してください」が有効だった（2025.05.17 時点）
- 結局 **CoT (Chain of Thought)** を読んで対応するので、限りなくプログラミングに近い思考が必要
  - 指示がどう解釈・実行されているのか確認するためにも **ユーザーは CoT を読むべき** 
  - Gemini 2.5 Pro(preview) にて `Chain of Thought を日本語で出力してください` が有効なのを確認（2025.05.17 時点）
- Gemini に「duckduckgo を使って」とお願いしたが、現在のツールでは検索エンジンが指定不可とのこと（2025.05.17 時点）
- Gemini にループ処理を指示した際、処理件数を増やすと 1 件あたりの精度を下げる傾向が見受けられた（2025.05.17 時点。CoT に言及は無かった）

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
