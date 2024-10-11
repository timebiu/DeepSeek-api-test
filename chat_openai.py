from openai import OpenAI
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['api_key']

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
  ],
    max_tokens=1024,
    temperature=0.7,
    stream=True
)

# print(response.choices[0].message.content)

# 处理流式输出
for chunk in response:
    if chunk.choices:
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end='', flush=True)

print()  # 打印换行符以结束输出