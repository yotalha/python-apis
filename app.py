import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('XRapidAPIKey')
api_host = os.environ.get('XRapidAPIHost')


headers = {
    'Accept': 'application/json',
    'X-RapidAPI-Key': api_key,
    'X-RapidAPI-Host': api_host
}

response = requests.get("https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random", headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data.get('value'))
else:
    print('some issue check')