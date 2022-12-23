from src.yatzy import Yatzy
import pytest

@pytest.mark.calcAll

def test_calcAll():

    assert Yatzy.calcTopSide(1,2,1,2,3) == [2,4,3]
    assert Yatzy.calcTopSide(2,2,2,2,6) == [6,12]
    assert Yatzy.calcTopSide(3,3,5,5,4) == [6,10,4]
