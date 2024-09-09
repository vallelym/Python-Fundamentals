import pytest
from pytest_files import count

def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

def test_count_integers():
    assert count([1, 2, 3, 4, 1, 1], 1) == 3
    assert count([1, 2, 3, 4, 1, 1], 2) == 1
    assert count([1, 2, 3, 4, 1, 1], 5) == 0

def test_count_strings():
    assert count(["apple", "banana", "apple", "cherry"], "apple") == 2
    assert count(["apple", "banana", "apple", "cherry"], "banana") == 1
    assert count(["apple", "banana", "apple", "cherry"], "grape") == 0
