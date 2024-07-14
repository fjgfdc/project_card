import logging


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_card(card_numb: str) -> str:
    """Return masked card(str)"""
    logger.info("Выполняем кодировку карты")
    return f"{card_numb[:4]} {card_numb[4:6]}{"*" * 2} {"*" * 4} {card_numb[12:]}"


def mask_account(account_number: str) -> str:
    """Return masked account number(str)"""
    logger.info("Выполняем кодировку номера счета")
    return f"{'*' * 2}{account_number[-4::]}"
