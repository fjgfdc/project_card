from src.masks import mask_account, mask_card


def masked(card: str) -> str:
    """Return mask of accounts and cards"""
    if "Счет" in card:
        new_acc = mask_account(card)
        return f"Счет {new_acc}"
    else:
        card_nums = mask_card(card[-16:])
        new_text = card.replace(card[-16:], card_nums)
        return new_text


def dated(time: str) -> str:
    """Return date"""
    return f"{time[8:10]}.{time[5:7]}.{time[:4]}"
