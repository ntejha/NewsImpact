import yfinance as yf
import json
import os

STOCK_FILE = os.path.join("data", "stocks.json")
with open(STOCK_FILE, "r") as f:
    STOCKS = json.load(f)

def fetch_prices():
    prices = {}
    for symbol in STOCKS:
        try:
            data = yf.Ticker(symbol).history(period="1d")
            prices[symbol] = data["Close"].iloc[-1] if not data.empty else 0
        except:
            prices[symbol] = 0
    return prices
