import json
import logging


logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def operations(file_path):
    """Возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            transactions = json.load(f)
            if isinstance(transactions, list):
                logger.info("Возвращает список с данными о  транзакциях")
                return transactions
            else:
                logger.error("Не являяется списком")
                return []
    except (json.JSONDecodeError, OSError):
        logger.error("произошла ошибка")
        return []
