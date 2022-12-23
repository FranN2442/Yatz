from src.yatzy import Yatzy
import pytest

@pytest.mark.fives

def testfives():

    assert Yatzy.fives(1,2,4,5,5) == 10
