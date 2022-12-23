import pytest
from src.yatzy import Yatzy

@pytest.mark.ones
def test_sacarUnos():

    assert Yatzy.ones(1,2,1,4,2) == 2