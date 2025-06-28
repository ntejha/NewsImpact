from sqlalchemy import create_engine, MetaData, Table, Column, String, Float
from configs.config import DATABASE_URL

engine = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT")
metadata = MetaData()

news_impact = Table(
    "news_impact", metadata,
    Column("symbol", String),
    Column("headline", String),
    Column("source", String),
    Column("sentiment", Float),
    Column("price", Float),
    Column("time", String),
)

metadata.create_all(engine)

def save_data(data):
    for row in data:
        row["sentiment"] = float(row["sentiment"])
        row["price"] = float(row["price"])
    with engine.connect() as conn:
        conn.execute(news_impact.insert(), data)