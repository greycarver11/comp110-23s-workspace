"""Ex04 - 'list' Utility Functions"""

__author__ = "730394136"

def all(list: list[int], number: int) -> bool:
    idx: int = 0
    while idx < len(list):
        if list[idx] != number:
            return False 
        idx += 1
    return True

def max(input: list[int]) -> int: 
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    while idx <= len(input):
        if len(max) == 3:
            return max[idx]

def is_equal(one: list[int], two: list[int]) -> bool:
    idx: int = 0
    while idx < len(one) and idx < len(two):
        if one[idx] != two[idx]:
            return False
        idx += 1
    return True
