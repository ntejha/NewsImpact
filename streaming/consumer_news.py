from kafka import KafkaConsumer
import json
import os
from textblob import TextBlob
from datetime import datetime
import pandas as pd

consumer = KafkaConsumer(
    'news-raw',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

bronze_path = 'data/bronze/news_raw.json'
silver_path = 'data/silver/news_clean.csv'
gold_path = 'data/gold/news_insight.csv'

# Ensure directories exist
os.makedirs('data/bronze', exist_ok=True)
os.makedirs('data/silver', exist_ok=True)
os.makedirs('data/gold', exist_ok=True)

bronze_data = []
silver_data = []

for msg in consumer:
    article = msg.value
    bronze_data.append(article)

    # Save to Bronze layer
    with open(bronze_path, 'w') as f:
        json.dump(bronze_data, f, indent=2)

    # Silver Layer: Clean + Sentiment
    title = article.get('title', '')
    description = article.get('description', '')
    text = title + " " + description
    sentiment = TextBlob(text).sentiment.polarity

    cleaned = {
        'title': title,
        'description': description,
        'publishedAt': article.get('publishedAt', ''),
        'source': article.get('source', {}).get('name', ''),
        'sentiment': sentiment
    }
    silver_data.append(cleaned)
    df_silver = pd.DataFrame(silver_data)
    df_silver.to_csv(silver_path, index=False)

    # Gold Layer: Simple Insight - Sentiment Aggregation
    df_gold = df_silver.groupby('source').agg({'sentiment': 'mean'}).reset_index()
    df_gold.columns = ['source', 'avg_sentiment']
    df_gold.to_csv(gold_path, index=False)

    print(f"[Consumer] Processed: {title} | Sentiment: {sentiment:.2f}")