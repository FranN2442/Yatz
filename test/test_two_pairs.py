from src.yatzy import Yatzy
import pytest

@pytest.mark.two_pairs
def test_two_pair():

    assert Yatzy.two_pair(1,1,2,3,2) == 6
    assert Yatzy.two_pair(1,1,4,3,2) == False