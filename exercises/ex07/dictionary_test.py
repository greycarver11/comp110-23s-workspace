"""Unit test for dictionary functions."""
__author__ = "730394136"

import pytest
from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests if dict is empty; edge case."""
    assert invert({}) == {}


def test_invert_one() -> None: 
    """Tests one input dictionary; use case."""
    test_apple: dict[str, str] = invert({'apple': 'cat'})
    assert invert(test_apple) == {'apple': 'cat'}


def test_invert_error() -> None:
    """Tests multiple keys; use case."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color_empty() -> None:
    """Tests if dict is empty; edge case."""
    assert favorite_color({}) == ""


def test_favorite_color_one() -> None:
    """Tests one instance; use case."""
    test_color: dict[str, str] = {"Marc": "yellow", "Tammy": "yellow"}
    assert favorite_color(test_color) == 'yellow'


def test_favorite_color_two() -> None: 
    """Tests two colors; use case."""
    test_color: dict[str, str] = {"Marc": "yellow", "Tammy": "purple", "Rocky": "yellow"}
    assert favorite_color(test_color) == 'yellow'


def test_count_empty() -> None:
    """Tests if list is empty; edge case."""
    assert count([]) == {}


def test_count_one() -> None:
    """Tests if list has one value; use case."""
    test_list: list[str] = ["hello"]
    assert count(test_list) == {'hello': 1}


def test_count_two() -> None:
    """Tests if list has two values; use case."""
    test_list: list[str] = ["hello", "goodbye"]
    assert count(test_list) == {'hello': 1, 'goodbye': 1}