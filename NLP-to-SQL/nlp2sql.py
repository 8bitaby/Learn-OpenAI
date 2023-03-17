import openai
import os
import pandas as pd
from dotenv import load_dotenv  # python-dotenv method
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

df = pd.read_csv("sales_data_sample.csv")
print(df.head())
