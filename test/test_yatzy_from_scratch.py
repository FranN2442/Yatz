import pytest
from src.yatzy import Yatzy


@pytest.fixture
def inyector():

    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada

