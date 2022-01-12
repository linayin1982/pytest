import os
import sys

sys.path.append(os.getcwd())

def pytest_configure(config):
    config.addinivalue_line("markers", "a: group a")
    config.addinivalue_line("markers", "b: group b")
    config.addinivalue_line("markers", "c: group c")
    config.addinivalue_line("markers", "must: group must")


