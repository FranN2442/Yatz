from src.yatzy import Yatzy
import pytest

@pytest.mark.fullhouse
def test_fullHouse():

    assert Yatzy.fullHouse(1,1,4,4,4) == 14
    assert Yatzy.fullHouse(1,2,2,3,3) == 0