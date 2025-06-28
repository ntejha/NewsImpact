# ingestion/producer.py
from ingestion.fetch_news import get_news
from ingestion.fetch_stocks import get_prices

def fetch_data():
    news_data = get_news()
    stock_data = get_prices()
    return news_data, stock_data

