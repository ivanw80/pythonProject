import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount=1"

payload = {}
headers = {
    "apikey": "bPjeymHfLTpbYLVTa6cmAoNMOs3vnUiF"
}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
results = data['result']
print(results)
