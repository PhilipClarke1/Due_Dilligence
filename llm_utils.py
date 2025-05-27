import openai
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def query_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"]

def query_claude(prompt):
    message = anthropic_client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        temperature=0.3,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text