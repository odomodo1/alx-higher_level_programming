#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            high = mid - 1
        else:
            return list_of_integers[mid]

    return list_of_integers[low]
