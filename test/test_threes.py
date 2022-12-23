from src.yatzy import Yatzy
import pytest


@pytest.mark.threes

def testThrees():

    assert Yatzy.threes(1,3,3,2,4) == 6