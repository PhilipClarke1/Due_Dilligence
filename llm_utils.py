import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
print("🔑 OPENAI_API_KEY from .env:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content

try:
    import anthropic
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    if ANTHROPIC_API_KEY:
        anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        def query_claude(prompt):
            message = anthropic_client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1024,
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
    else:
        def query_claude(prompt):
            return "Claude API key not found. Skipping."
except ImportError:
    def query_claude(prompt):
        return "Anthropic SDK not installed."
