def mask_card(card_numb: str) -> str:
    """Return masked card(str)"""
    return f"{card_numb[:4]} {card_numb[4:6]}{"*" * 2} {"*" * 4} {card_numb[12:]}"


def mask_account(account_number: str) -> str:
    """Return masked account number(str)"""
    return f"{'*' * 2}{account_number[-4::]}"
