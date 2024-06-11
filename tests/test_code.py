import pytest
from src.widget import mask


@pytest.fixture
def cards():
    return "Visa Platinum 7000 7922 8960 6361"


@pytest.fixture
def user():
    return "Счет 73654108430135874305"


def test_mask(cards, user):
    assert mask(cards) == "Visa Platinum 7000 79** **** 6361"
    assert mask(user) == "Счет **4305"
