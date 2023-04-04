import openai
import os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from dotenv import load_dotenv  # python-dotenv method
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
df = pd.read_csv("sales_data_sample.csv")

# Creates a temp database inside RAM
temp_db = create_engine('sqlite:///:memory:', )
data = df.to_sql(name='Sales', con=temp_db)

# Make the database connection perfom actions
with temp_db.connect() as conn:
    result = conn.execute(text("SELECT SUM(SALES) FROM Sales"))

# https://platform.openai.com/examples/default-sql-translate


def create_table_definition(df):
    prompt = """### sqlite SQL tables, with their properties:
    #
    # Sales({})
    #
    """.format(",".join(str(col)for col in df.columns))
    return prompt


def prompt_input():
    nlp_text = input("Enter the information you want")
    return nlp_text


def combine_prompts(df, query_prompt):
    definition = create_table_definition(df)
    query_init_string = f'### A query to answer: {query_prompt}\nSELECT'
    print(definition+query_init_string)
    return definition+query_init_string


nlp_text = prompt_input()


response = openai.Completion.create(
    model='text-davinci-003',
    prompt=combine_prompts(df, nlp_text),
    temperature=0,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0,
    presence_penalty=0,
    stop=['#', ';'])

print(response['choices'][0]['text'])


def handle_response(response):
    query = response['choices'][0]['text']
    query = "SELECT"+query
    return query
