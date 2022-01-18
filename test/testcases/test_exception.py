import pytest

def test_recursion_depth():
    print("hello")
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    print(str(excinfo.value))
    assert "maximum recursion" in str(excinfo.value)

def test_simple():
    set1 = set(("1308"))
    set2 = set(("8031"))
    assert set1 == set2