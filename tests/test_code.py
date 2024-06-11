import pytest
from src.masks import mask_account, mask_card


@pytest.fixture
def cards():
    return "7000792289606361"


@pytest.fixture
def user():
    return "73654108430135874305"


def test_masks(cards, user):
    assert mask_card(cards) == "7000 79** **** 6361"
    assert mask_account(user) == "**4305"
