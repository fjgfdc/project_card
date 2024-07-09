import os
import requests


def amount_transaction(transaction):
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = float(transaction["amount"])
    currency = transaction["currency"]
    if currency == "RUB":
        return amount

    elif currency != "RUB":
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return float(data["result"])

    else:
        raise ValueError(f"Неизвестная валюта {currency}")
