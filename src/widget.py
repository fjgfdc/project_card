from masks import mask_account, mask_card


def mask(card: str) -> str:
    if "Счет" in card:
        return mask_account(card)
    else:
        card_nums = mask_card(card[-16:])
        new_text = card.replace(card[-16:], card_nums)
        return new_text


def date(time: str) -> str:
    return f"{time[8:10]}.{time[6:7]}.{time[:4]}"
