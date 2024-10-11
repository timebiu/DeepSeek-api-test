import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['api_key']

url = "https://api.deepseek.com/beta/completions"

payload = json.dumps({
  "model": "deepseek-chat",
  "prompt": "有一天, ",
  "echo": False,
  "frequency_penalty": 0,
  "logprobs": 0,
  "max_tokens": 1024,
  "presence_penalty": 0,
  "stop": None,
  "stream": False,
  "stream_options": None,
  "suffix": None,
  "temperature": 1,
  "top_p": 1
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer ' + api_key
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)