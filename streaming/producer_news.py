from kafka import KafkaProducer
import json
from newsapi import NewsApiClient
import time
from dotenv import load_dotenv
import os 

load_dotenv()

api = os.getenv("NEWS_API_KEY")

newsapi = NewsApiClient(api_key=api)
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = 'news-raw'

while True:
    top_headlines = newsapi.get_top_headlines(language='en', page_size=5)
    for article in top_headlines['articles']:
        producer.send(TOPIC, article)
        print("[Producer] Sent article:", article['title'])
    time.sleep(60)  # fetch every minute