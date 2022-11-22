import requests
import pandas as pd

url = "https://api.apilayer.com/currency_data/live?base=USD&symbols=EUR,GBP"

payload = {}
headers= {
  "apikey": "0NZF0kOcyHlYt8OvOVuGJMYLVbl6My29"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result.to_csv("save_data_exchange.csv"))
#print(result)
