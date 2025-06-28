from ingestion.fetch_news import fetch_news
from ingestion.fetch_stocks import fetch_prices
from processing.sentiment import analyze_sentiment
from processing.correlate import correlate_news_stock
from storage.db import save_data

def run_pipeline():
    print("📥 Fetching news...")
    news = fetch_news()

    print("💹 Fetching stock prices...")
    prices = fetch_prices()

    print("🧠 Performing sentiment analysis...")
    news = analyze_sentiment(news)

    print("🔗 Matching news to stock prices...")
    merged = correlate_news_stock(news, prices)

    if not merged:
        print("⚠️ No matched data found — check symbol match or news content.")
        return

    print(f"💾 Saving {len(merged)} records...")
    save_data(merged)

    print("✅ Pipeline completed.")
    print("📊 First 5 records:")
    for row in merged[:5]:
        print({
            "symbol": row["symbol"],
            "sentiment": row["sentiment"],
            "headline": row["headline"]
        })

if __name__ == "__main__":
    run_pipeline()
