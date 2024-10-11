import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['api_key']

url = "https://api.deepseek.com/user/balance"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer ' + api_key
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)