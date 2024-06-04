import masks


def masks(card: str) -> str:
    if "Счет" in card:
     return mask_account(card)
    else:
        card_nums = mask_card(card[-16:])
        new_text = card.replace(card[-16:], card_nums)
        return new_text
