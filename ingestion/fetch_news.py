# ingestion/fetch_news.py

import requests
from configs.config import NEWS_API_KEY

def fetch_news():
    if not NEWS_API_KEY:
        print("⚠️ NEWS_API_KEY not set in config")
        return []

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"category=business&language=en&pageSize=10&apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Failed to fetch news: {response.status_code}")
        return []

    articles = response.json().get("articles", [])
    results = []
    for article in articles:
        results.append({
            "headline": article.get("title", ""),
            "source": article.get("source", {}).get("name", ""),
            "time": article.get("publishedAt", "")
        })
    return results
