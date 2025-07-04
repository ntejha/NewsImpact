import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(page_title="News Mood Tracker", layout="centered")

st.title("📰 News Mood Tracker")
st.subheader("Live sentiment of different news sources")

gold_path = "data/gold/news_insight.csv"

def load_data():
    if os.path.exists(gold_path):
        df = pd.read_csv(gold_path)
        df = df.sort_values(by="avg_sentiment", ascending=False)
        return df
    return pd.DataFrame(columns=["source", "avg_sentiment"])

def get_sentiment_emoji(score):
    if score >= 0.5:
        return "😊"
    elif score >= 0.0:
        return "😐"
    else:
        return "😞"

refresh_rate = st.slider("How often should this update? (seconds)", 10, 120, 60)
placeholder = st.empty()

while True:
    with placeholder.container():
        df = load_data()

        if df.empty:
            st.warning("Waiting for news data...")
        else:
            df["Mood"] = df["avg_sentiment"].apply(get_sentiment_emoji)

            st.markdown("### 🏆 Top 3 Most Positive Sources")
            st.table(df.head(3)[["source", "avg_sentiment", "Mood"]])

            st.markdown("### 🚨 Bottom 3 Least Positive Sources")
            st.table(df.tail(3).sort_values(by="avg_sentiment")[["source", "avg_sentiment", "Mood"]])

            st.markdown("### 📊 All Sources")
            st.dataframe(df.set_index("source"), use_container_width=True)

            st.markdown("### 📈 Mood Chart")
            st.bar_chart(df.set_index("source")["avg_sentiment"])

            st.download_button("Download Sentiment CSV", df.to_csv(index=False), file_name="news_sentiment.csv")

    time.sleep(refresh_rate)
    st.rerun()
