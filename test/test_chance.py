from src.yatzy import Yatzy
import pytest

@pytest.mark.chance
def test_chance():

    assert Yatzy.chance(1,2,3,4,5) == 15
    assert Yatzy.chance(1,3,6,5,5) == 20
    assert Yatzy.chance(2,5,6,4,6) == 23