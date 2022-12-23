from src.yatzy import Yatzy
import pytest

@pytest.mark.cuatroIguales
def test_four_of_a_kind():

    assert Yatzy.four_of_a_kind(2,2,3,2,2) == 8
    assert Yatzy.four_of_a_kind(1,4,4,4,4) == 16

    assert Yatzy.four_of_a_kind(1,2,2,2,3) == None