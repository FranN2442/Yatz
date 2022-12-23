from src.yatzy import Yatzy
import pytest

@pytest.mark.largeStreight
def test_largeStreight():

    assert Yatzy.largeStraight(2,3,4,5,6) == 20

    assert Yatzy.largeStraight(1,2,3,4,6) == 0