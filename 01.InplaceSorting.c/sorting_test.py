"""
Unit tests for 00.Demo
"""

import random
from itertools import pairwise
import pytest
import sortings


@pytest.fixture(scope="module")
def fatal_array():
    """
    Setup function to create shuffled array
    """
    r = random.Random()
    r.seed(123456)

    data = list(range(1000))
    r.shuffle(data)
    yield data


def test_builtin_sort_array(fatal_array):
    """
    Test standard library sorting
    """
    sortings.builtin_sort(fatal_array)
    is_sorted = all(x <= y for x, y in pairwise(fatal_array))
    assert is_sorted


@pytest.fixture(scope="module")
def random_test_array():
    """Create shuffled array for testing"""
    r = random.Random()
    r.seed(42)
    data = list(range(100))
    r.shuffle(data)
    return data


def test_bubble_sort(random_test_array):
    """Test bubble sort algorithm"""
    arr = random_test_array.copy()
    sortings.bubble_sort(arr)
    is_sorted = all(x <= y for x, y in pairwise(arr))
    assert is_sorted


def test_quick_sort(random_test_array):
    """Test quick sort algorithm"""
    arr = random_test_array.copy()
    sortings.quick_sort(arr)
    is_sorted = all(x <= y for x, y in pairwise(arr))
    assert is_sorted


def test_bubble_sort_empty():
    """Bubble sort with empty array"""
    arr = []
    sortings.bubble_sort(arr)
    assert arr == []


def test_quick_sort_single():
    """Quick sort with single element"""
    arr = [42]
    sortings.quick_sort(arr)
    assert arr == [42]


def test_bubble_sort_already_sorted():
    """Bubble sort on already sorted array"""
    arr = [1, 2, 3, 4, 5]
    sortings.bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_quick_sort_reverse():
    """Quick sort on reverse sorted array"""
    arr = [5, 4, 3, 2, 1]
    sortings.quick_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_bubble_sort_duplicates():
    """Bubble sort with duplicate values"""
    arr = [3, 1, 3, 2, 1, 2]
    sortings.bubble_sort(arr)
    assert arr == [1, 1, 2, 2, 3, 3]


def test_quick_sort_negative():
    """Quick sort with negative numbers"""
    arr = [-3, 5, -1, 0, 2, -2]
    sortings.quick_sort(arr)
    assert arr == [-3, -2, -1, 0, 2, 5]
