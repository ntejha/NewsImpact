import json
import os

STOCK_FILE = os.path.join("data", "stocks.json")
with open(STOCK_FILE, "r") as f:
    STOCKS = json.load(f)

def correlate_news_stock(news, prices):
    matched = []
    for item in news:
        headline = item["headline"].lower()
        for symbol, name in STOCKS.items():
            if name.lower() in headline:
                matched.append({
                    "symbol": symbol,
                    "headline": item["headline"],
                    "source": item["source"],
                    "sentiment": item["sentiment"],
                    "price": prices.get(symbol, 0),
                    "time": item["time"]
                })
    return matched
