"""Collect URLs."""

import asyncio
from langchain_openai import ChatOpenAI
from browser_use import Agent

async def main():
    """execute"""
    agent = Agent(
        task=(
            "あなたは企業のURL調査を担当するエージェントで、WEBからコーポレートサイトのURLを収集します。\n"
            "- https://duckduckgo.com/?q=<検索キーワード>&t=h_&ia=answers を開いて開始してください\n"
            "- 検索キーワードに該当するコーポレートサイトのURLを取得してください\n"
            "- 以下を検索キーワードに付与してください\n"
            "  * -beautifyjp.net -beauty-job.biz -beauty.biglobe.ne.jp -beauty.hotpepper.jp "
            "    -beauty.rakuten.co.jp -biyousitu.yu-nagi.com -blogtag.ameba.jp -hairbook.jp "
            "    -hairlog.jp -hermo-style.com -kireistyle-woman.com -map.yahoo.co.jp "
            "    -minimodel.jp -page.line.me -zouri.jp -web.fc2.com -stylelog.tokyo "
            "    -www.ameba.jp -www.beauty-park.jp -www.ekiten.jp -www.instagram.com  "
            "    -www.navitime.co.jp -www.yelp.com\n"
            "    -ホットペッパービューティー、案内サイト、美容室の口コミサイト、ポータルサイト、地図、ブログなど、"
            "コーポレートサイト以外を除外してください\n"
            "- コーポレートサイトのトップページのURLのみを取得してください\n"
            "- コーポレートサイトが見つからなかった場合はコーポレートサイトURLの取得結果を「該当URLなし」としてください\n"
            "- google にはアクセスしないでください\n"
            "- 1件毎にブラウザのタブを閉じてください\n"
            "\n"
            "以下の検索キーワードを使用してください:\n"
            "- ほげほげ\n"
            "- hoge\n"
            "- ふがふが\n"
            "\n"
            "下記の形式を一行とした一覧でデータを返してください:\n"
            "<検索キーワード> <コーポレートサイトURLの取得結果>\n"
        ),
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    result_text = result.final_result()
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(str(result_text))

asyncio.run(main())
