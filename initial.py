import openai
import os
from dotenv import load_dotenv  # python-dotenv method
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
response = openai.Completion.create(
    model='text-davinci-003',
    prompt='Give me two reasons to learn OpenAI API with python',
    max_tokens=300)
print(response)
