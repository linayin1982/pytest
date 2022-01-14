import os
import sys
from src.util.foo import Foo

sys.path.append(os.getcwd())

def pytest_configure(config):
    config.addinivalue_line("markers", "a: group a")
    config.addinivalue_line("markers", "b: group b")
    config.addinivalue_line("markers", "c: group c")
    config.addinivalue_line("markers", "must: group must")

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return ["Comparing Foo instances:"," vals: {} != {}".format(left.val, right.val)]



