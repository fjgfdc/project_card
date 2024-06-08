from typing import Iterable


def filter_by_state(state_list: Iterable, normal_state: str = "EXECUTED") -> Iterable:
    """Return filtered list by state"""
    total_list = []
    for dict_list in state_list:
        if dict_list.get("state") == normal_state:
            total_list.append(dict_list)
    return total_list


def sort_by_date(date_list: Iterable, reverse_list: bool = True) -> Iterable:
    """Return filtered list by date"""
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)
    return sorted_list
