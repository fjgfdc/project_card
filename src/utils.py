import json


def operations(file_path='..\\data\\operations.json'):
    """Возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            transactions = json.load(f)
            if isinstance(transactions, list):
                return transactions
            else:
                return []
    except (json.JSONDecodeError, OSError):
        return []
