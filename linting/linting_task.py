"""
This module contains a function to count the occurrences of an item in a sequence.
"""

def count(sequence, item):
    """
    Count the number of occurrences of item in sequence.

    Args:
        sequence (list): The list to search through.
        item: The item to count in the list.

    Returns:
        int: The number of occurrences of item in the list.
    """
    count_occurrences = 0
    for element in sequence:
        if element == item:
            count_occurrences += 1
    return count_occurrences
