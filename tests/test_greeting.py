from greeting import my_name

import pytest

@pytest.fixture
def bob():
    return "My name is: Bob"

@pytest.fixture
def sally():
    return "My name is: Sally"

def test_bob(bob):
    assert bob == my_name("Bob")

def test_sally(sally):
    assert sally == my_name("Sally")