from src.util.foo import Foo

def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2
