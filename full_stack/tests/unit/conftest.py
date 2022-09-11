import pytest


@pytest.fixture
def amount_staked():
    return Web3.toWei(1, "ether")
