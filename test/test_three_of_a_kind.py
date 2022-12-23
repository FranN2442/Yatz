from src.yatzy import Yatzy
import pytest

@pytest.mark.tresIguales
def test_three_of_a_kind():

    assert Yatzy.three_of_a_kind(1,3,4,1,1) == 3
    assert Yatzy.three_of_a_kind(1,2,3,2,2) == 6
    assert Yatzy.three_of_a_kind(1,3,5,5,5) == 15

    assert Yatzy.three_of_a_kind(1,2,3,4,5) == None



    

