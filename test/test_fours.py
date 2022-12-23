from src.yatzy import Yatzy
import pytest

@pytest.mark.fours
def test_fours():
    
    assert Yatzy.fours(4,4,1,2,5) == 8