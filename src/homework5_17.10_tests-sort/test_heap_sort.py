# test_heap_sort.py
import pytest
from heap_sort import heap_sort

# простые тесты

def test_basic_sort():
    """Самый простой тест - обычный случай"""
    arr = [4, 2, 8, 1, 5]
    result = heap_sort(arr.copy())
    assert result == [1, 2, 4, 5, 8]

def test_already_sorted():
    """Тест с уже отсортированным массивом"""
    arr = [1, 2, 3, 4, 5]
    result = heap_sort(arr.copy())
    assert result == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Тест с обратным порядком"""
    arr = [5, 4, 3, 2, 1]
    result = heap_sort(arr.copy())
    assert result == [1, 2, 3, 4, 5]

# Тесты крайних случаев

def test_empty_array():
    """Тест пустого массива"""
    arr = []
    result = heap_sort(arr.copy())
    assert result == []

def test_single_element():
    """Тест с одним элементом"""
    arr = [42]
    result = heap_sort(arr.copy())
    assert result == [42]

def test_two_elements():
    """Тест с двумя элементами"""
    # Уже отсортирован
    assert heap_sort([1, 2]) == [1, 2]
    # Не отсортирован
    assert heap_sort([2, 1]) == [1, 2]

def test_all_same_elements():
    """Тест когда все элементы одинаковые"""
    arr = [5, 5, 5, 5, 5]
    result = heap_sort(arr.copy())
    assert result == [5, 5, 5, 5, 5]

# 3. Тесты с особенными данными

def test_with_duplicates():
    """Тест с повторяющимися числами"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result = heap_sort(arr.copy())
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert result == expected

def test_negative_numbers():
    """Тест с отрицательными числами"""
    arr = [-3, -1, -5, 0, 2, -2]
    result = heap_sort(arr.copy())
    expected = [-5, -3, -2, -1, 0, 2]
    assert result == expected

def test_mixed_numbers():
    """Тест со смешанными числами"""
    arr = [10, -5, 0, 3, -2, 7]
    result = heap_sort(arr.copy())
    expected = [-5, -2, 0, 3, 7, 10]
    assert result == expected
