import requests
import pandas as pd
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

url = "https://api.apilayer.com/currency_data/live?base=USD&symbols=EUR,GBP"


PAYLOAD = json.loads(os.getenv("PAYLOAD"))  
HEADERS = json.loads(os.getenv("HEADERS"))

response = requests.request("GET", url, headers=HEADERS, data = PAYLOAD)

status_code = response.status_code
result = response.text



