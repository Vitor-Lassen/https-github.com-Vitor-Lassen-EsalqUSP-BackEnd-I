import requests

response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

dados = response.json()

taxa_dollar = dados["USDBRL"]["bid"]

print(f"Taxa do dólar: {taxa_dollar}")
