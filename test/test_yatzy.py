from src.yatzy import Yatzy
import pytest

@pytest.mark.yatzy

def test_yatzy():

    assert Yatzy.yatzy(1,1,1,1,1) == 55
    assert Yatzy.yatzy(2,2,2,2,2) == 60
    assert Yatzy.yatzy(3,3,3,3,3) == 65
    assert Yatzy.yatzy(4,4,4,4,4) == 70
    assert Yatzy.yatzy(5,5,5,5,5) == 75
    assert Yatzy.yatzy(6,6,6,6,6) == 80

    assert Yatzy.yatzy(1,1,1,1,3) == 0