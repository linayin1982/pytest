import pytest
from util import algo


@pytest.mark.must
@pytest.mark.parametrize("data,expected",[((2,4,7,1,5,6),1),((5, -2, 0, 9, 12), -2), ((200, 100, 0, 300, 400), 0)])
def test_min(data,expected):
    assert algo.min(data) == expected

@pytest.mark.parametrize("data,expected",[((2, 3, 1, 4, 6), 6), ((5, -2, 0, 9, 12), 12), ((200, 100, 0, 300, 400), 400)])
@pytest.mark.must
def test_max(data,expected):
    assert algo.max(data) == expected

@pytest.mark.skip
def test_a1():
    assert (1) == (1)

@pytest.mark.a
def test_a2():
    assert (1) == (1)

@pytest.mark.a
def test_a3():
    assert (1) == (1)

@pytest.mark.b
def test_b1():
    assert (1) == (1)

@pytest.mark.b
def test_b2():
    assert (1) == (1)