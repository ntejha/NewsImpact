from textblob import TextBlob

def analyze_sentiment(news_list):
    for item in news_list:
        blob = TextBlob(item["headline"])
        item["sentiment"] = blob.sentiment.polarity
    return news_list
