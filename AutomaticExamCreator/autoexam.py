import os
import openai
from dotenv import load_dotenv  # python-dotenv method
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
