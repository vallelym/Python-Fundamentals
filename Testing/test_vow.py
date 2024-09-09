import pytest
from pytest_files import vowels

def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels

def test_vowels():
    assert vowels("hello") == 2
    assert vowels("world") == 1
    assert vowels("AEIOU") == 5
    assert vowels("bcdfg") == 0
    assert vowels("Python") == 1
    assert vowels("") == 0
