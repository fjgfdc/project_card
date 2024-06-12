
def filter_by_state(state_list: list[dict], normal_state: str = "EXECUTED") -> list[dict]:
    """Return filtered list by state"""
    total_list = []
    for dict_list in state_list:
        if dict_list.get("state") == normal_state:
            total_list.append(dict_list)
    return total_list


def sort_by_date(date_list: list[dict], reverse_list: bool = True) -> list[dict]:
    """Return filtered list by date"""
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)
    return sorted_list


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]))
