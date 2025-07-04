import pandas as pd
import os

silver_path = 'data/silver/news_clean.csv'
gold_path = 'data/gold/news_insight.csv'

if not os.path.exists(silver_path):
    print("Silver layer not found.")
    exit(1)

df = pd.read_csv(silver_path)

df_gold = df.groupby('source').agg({'sentiment': 'mean'}).reset_index()
df_gold.columns = ['source', 'avg_sentiment']
df_gold.to_csv(gold_path, index=False)

print("Gold layer updated:", df_gold.shape)
