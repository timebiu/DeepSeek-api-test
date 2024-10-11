from openai import OpenAI
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['api_key']

# user should set `base_url="https://api.deepseek.com/beta"` to use this feature.
client = OpenAI(
  api_key=api_key,
  base_url="https://api.deepseek.com/beta",
)
response = client.completions.create(
  model="deepseek-chat",
  prompt="def fib(a):",
  suffix="    return fib(a-1) + fib(a-2)",
  max_tokens=128)
print(response.choices[0].text)