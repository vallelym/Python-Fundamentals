import pytest
from pytest_files import factorial

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def test_fact():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(3) == 6
    assert fact(4) == 24
    assert fact(5) == 120
    assert fact(10) == 3628800
