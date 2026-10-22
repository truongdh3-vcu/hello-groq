import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"],
)

MODEL = "openai/gpt-oss-120b"

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "A store made $40 profit yesterday, tomorrow the profit is 25% more - what is the profit tomorrow?"}],
    reasoning_effort="medium",
)

print(response.choices[0].message.content)
print(response.usage)