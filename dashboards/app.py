import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from configs.config import DATABASE_URL
import altair as alt

st.set_page_config(page_title="News Impact Dashboard", layout="wide")
st.title("📰 Real-Time News Impact on Stock Prices")


engine = create_engine(DATABASE_URL)
query = "SELECT * FROM news_impact"
df = pd.read_sql(query, engine)

if df.empty:
    st.warning("No data found. Run the pipeline to ingest data.")
    st.stop()

df["time"] = pd.to_datetime(df["time"])
df["date"] = df["time"].dt.date


df = df[df["sentiment"].abs() >= 0.05]

if df.empty or df["sentiment"].abs().mean() < 0.05:
    st.warning("Sentiment too neutral. Run the pipeline with better headline relevance.")
    st.stop()

st.subheader("📊 1. News Headline Coverage Count")
st.bar_chart(df["symbol"].value_counts())

st.subheader("📈 2. Average Sentiment Per Stock")
avg_sentiment = df.groupby("symbol")["sentiment"].mean().sort_values()
st.bar_chart(avg_sentiment)

st.subheader("📆 3. Sentiment Trend Over Time")
trend = df.groupby(["date", "symbol"])["sentiment"].mean().unstack()
st.line_chart(trend)

st.subheader("💹 4. Price vs Sentiment Scatter")
scatter = alt.Chart(df).mark_circle(size=70, opacity=0.6).encode(
    x="sentiment",
    y="price",
    color="symbol",
    tooltip=["symbol", "headline", "sentiment", "price"]
).interactive()
st.altair_chart(scatter, use_container_width=True)

st.subheader("🧠 5. Top Bullish and Bearish Headlines")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🟢 Bullish")
    top_pos = df.sort_values("sentiment", ascending=False).head(5)
    st.table(top_pos[["symbol", "headline", "sentiment"]])

with col2:
    st.markdown("### 🔴 Bearish")
    top_neg = df.sort_values("sentiment", ascending=True).head(5)
    st.table(top_neg[["symbol", "headline", "sentiment"]])

with st.expander("📋 Full Raw Data"):
    st.dataframe(df.sort_values("time", ascending=False), use_container_width=True)
