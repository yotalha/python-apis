import requests

headers = {
    'Accept': 'application/json',
    'X-RapidAPI-Key': '7108201eafmshb996c2557120670p1c1f3bjsnae663a89ba7f',
    'X-RapidAPI-Host': 'matchilling-chuck-norris-jokes-v1.p.rapidapi.com'
}

response = requests.get("https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random", headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data.get('value'))
else:
    print('some issue check')