import pytest
from src.yatzy import Yatzy

@pytest.mark.smallStreight
def testSmallStreight():

    assert Yatzy.smallStraight(1,2,3,4,5) == 15
    
    assert Yatzy.smallStraight(2,1,3,4,6) == 0
    assert Yatzy.smallStraight(1,1,2,3,4) == 0