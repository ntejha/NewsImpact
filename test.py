# test_db.py
from sqlalchemy import create_engine
import pandas as pd
from configs.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
df = pd.read_sql("SELECT * FROM news_impact", con=engine)
print(df.head())

