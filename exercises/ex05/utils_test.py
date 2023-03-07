"""Unit test for utils functions."""
__author__ = "730394136"

from exercises.ex05.utils import only_evens, sub, concat


def test_even_empty() -> None:
    """Tests if list is empty; edge case."""
    assert only_evens([]) == []


def test_even_one() -> None:
    """Tests one number; use case."""
    test_list: list[int] = [1]
    assert only_evens(test_list) == []


def test_even_many() -> None:
    """Tests all numbers in list, returns even number; use case."""
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]


def test_sub_empty() -> None:
    """Tests if list is empty; edge case."""
    assert sub([], 0, 0) == []


def test_sub_one() -> None:
    """Tests one number; use case."""
    test_list: list[int] = [5]
    assert sub(test_list, 0, 1) == [5]


def test_sub_many() -> None:
    """Tests all numbers in list, returns even number; use case."""
    test_list: list[int] = [10, 20, 30, 40]
    assert sub(test_list, 1, 3) == [20, 30]


def test_con_empty() -> None:
    """Tests if list is empty; edge case."""
    assert concat([], []) == []


def test_con_one() -> None:
    """Tests one number; use case."""
    test_list1: list[int] = [2]
    test_list2: list[int] = [4]
    assert concat(test_list1, test_list2) == [2, 4]


def test_con_many() -> None:
    """Tests all numbers in list, returns even number; use case."""
    test_list1: list[int] = [2, 3]
    test_list2: list[int] = [4, 5]
    assert concat(test_list1, test_list2) == [2, 3, 4, 5]