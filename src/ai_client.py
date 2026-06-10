import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def ask_ai(prompt):
    message = client.messages.create(
        model="claude-3-5-haiku-latest",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text