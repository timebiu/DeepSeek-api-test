from openai import OpenAI
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['api_key']

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com/beta",
)

messages = [
    {"role": "user", "content": "Please write quick sort code"},
    {"role": "assistant", "content": "```python\n", "prefix": True}
]
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    stop=["```"],
)
print(response.choices[0].message.content)