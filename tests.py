import pytest


#3 теста на int: вычитание, степень, 
#смена знака (параметры: отриц, положит, ноль(негативный), возле ноля)


def test_diff():
    assert 5-2==3

def test_pow():
    assert 2**3==8

@pytest.mark.parametrize("input,expected", [(10, -10), (-1, 1), (0, 0),(1, -1),(-10, 10)])
def test_neg(input, expected):
    assert -input == expected

#3 теста на float: сумма, модуль, округление

def test_summ():
    assert 0.4+0.6==1

def test_abs():
    assert abs(-0.5)==0.5

def test_round():
    assert round(1.1)==1