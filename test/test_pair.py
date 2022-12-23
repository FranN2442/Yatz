from src.yatzy import Yatzy
import pytest


@pytest.mark.pair
def test_score_pair():

    assert Yatzy.score_pair(1,2,3,5,2) == 4
    assert Yatzy.score_pair(1,1,2,3,2) == False