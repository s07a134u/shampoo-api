import requests
import json
import pandas as pd
import csv
from pathlib import Path


def RakutenAPI():
    API_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"
    APP_ID = "1050828393533447221"   #作成したアプリID
    OUTPUT_CSV = "shampoo.csv"   #出力するファイル

    #検索する商品の設定
    params = {
            "applicationId": APP_ID,
            "keyword": "シャンプー",
            "hits": "30"
    }
    print("商品を検索しています")
    response = requests.get(API_URL, params=params)
    
    if response.status_code != 200 :
            print(f"リクエストに失敗しました。ステータスコード：{response.status_code}")
            raise RuntimeError(f"HTTP {response.status_code}")

    data = response.json()
    items = data.get("Items", [])

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["商品名","ジャンルID", "価格","URL","店名"])  

        for item in items:
            info = item.get("Item",item)

            #欲しい情報を取り出す
            name = info.get("itemName","(不明)")
            genre_id = info.get("genreId")
            price = info.get("itemPrice")
            url = info.get("itemUrl", "(なし)")
            shop = info.get("shopName", "(不明)")

            #CSVに商品情報を追加
            writer.writerow([name, genre_id, price, url, shop])
                    
            # 表示（価格が数値でない場合のフォールバックも用意）
            price_str = f"¥{price}" if isinstance(price, (int, float)) else "(価格不明)"
            print(f"{name} / {price_str}")
            print(f"ショップ: {shop}")
            print(f"URL: {url}")
            print("-" * 40)


    
    print("ファイルを保存しました")
    return OUTPUT_CSV