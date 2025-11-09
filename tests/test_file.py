from src.main import *

def test_function():
    assert function("a","b","c") == "abc"

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(2,0) == 0
