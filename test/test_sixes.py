from src.yatzy import Yatzy
import pytest


@pytest.mark.sixes
def testSixes():

    assert Yatzy.sixes(1,6,2,6,4) == 12