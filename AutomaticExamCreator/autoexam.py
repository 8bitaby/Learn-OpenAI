import os
import openai
from dotenv import load_dotenv  # python-dotenv method
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def create_test_prompt(topic, num_questions, num_possible_answers):
    prompt = f"Create a multiple choice quiz on the topic of {topic} consisting of {num_questions} questions. " \
        + f"Each question should have {num_possible_answers} options. "\
        + f"Also include the correct answer for each question using the starting string 'Correct Answer: '."
    return prompt


prompt = create_test_prompt('Kerala History', 5, 3)

response = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,)

print(response['choices'][0]['text'])
