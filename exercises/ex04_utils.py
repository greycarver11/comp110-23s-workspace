"""Ex04 - 'list' Utility Functions."""
__author__ = "730394136"


def all(list: list[int], number: int) -> bool:
    """Returns True when number is found in list."""
    idx: int = 0
    if len(list) == 0:
        return False
    while idx < len(list):
        if list[idx] != number:
            return False 
        idx += 1
    return True


def max(input: list[int]) -> int: 
    """Returns max number when given a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    max_temp: int = input[idx]
    while idx < len(input):
        if max_temp < input[idx]:
            max_temp = input[idx]
        idx += 1
    return max_temp 


def is_equal(one: list[int], two: list[int]) -> bool:
    """Returns True when two lists equal each other."""
    idx: int = 0
    if len(one) != len(two):
        return False
    if len(one) == 0 and len(two) == 0:
        return True
    while idx < len(one) and idx < len(two):
        if one[idx] != two[idx]:
            return False
        idx += 1
    return True