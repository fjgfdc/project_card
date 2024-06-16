import pytest
from src.masks import mask_account, mask_card
from src.processing import filter_by_state, sort_by_date
from src.widget import masked, dated
from src.generators import transactions, filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def cards():
    return "7000792289606361"


@pytest.fixture
def user():
    return "73654108430135874305"


@pytest.fixture
def date():
    return "2018-07-11T02:26:18.671407"


def test_masks(cards, user):
    assert mask_card(cards) == "7000 79** **** 6361"
    assert mask_account(user) == "**4305"


@pytest.mark.parametrize("n, expected", [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
 [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
                                          ),
                                         ([{}], [])])
def test_filter_by_state(n, expected):
    assert filter_by_state(n) == expected


@pytest.mark.parametrize("n, expected", [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
 [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
                                          ),
                                         ([{}], [{}])])
def test_sort_by_date(n, expected):
    assert sort_by_date(n) == expected


@pytest.mark.parametrize("x, expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                         ("Счет 73654108430135874305", "Счет **4305")])
def test_add(x, expected):
    assert masked(x) == expected


def teste_dated(date):
    assert dated(date) == "11.07.2018"


def teste_filter_by_currency():
    assert next(filter_by_currency(transactions, "USD")) == 939719570


def teste_transaction_descriptions():
    assert next(transaction_descriptions(transactions)) == "Перевод организации"


def teste_card_number_generator():
    assert next(card_number_generator(1, 1)) == "0000 0000 0000 0001"
