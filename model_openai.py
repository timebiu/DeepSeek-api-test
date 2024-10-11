from openai import OpenAI
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['api_key']

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
print(client.models.list())