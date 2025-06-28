# NewsImpact

This project simulates a real-time pipeline that ingests business news headlines, analyzes their sentiment, and matches them with corresponding stock prices. It helps explore how media sentiment might influence market behavior.

## 🔍 What It Does

- Fetches live business news headlines
- Applies sentiment analysis on the headlines
- Maps each news item to stocks it refers to
- Collects latest stock prices for matched tickers
- Stores everything in a PostgreSQL database
- Visualizes the data in an interactive Streamlit dashboard

## 📦 Key Components

- `main.py`: Runs the complete data pipeline
- `configs/`: Contains database config
- `ingestion/`: Handles fetching of news and stock prices
- `processing/`: Sentiment analysis and correlation logic
- `storage/`: PostgreSQL connection and saving
- `dashboards/app.py`: Streamlit interface for insights

---

