# tests2.py
import pytest
import random
from other_sorts import bubble_sort, selection_sort, python_sort
from heap_sort import heap_sort

# 1. Основное свойство: ВСЕ ТРИ сортировки дают одинаковый результат

def test_all_three_sorts_same_result_simple():
    """Все три сортировки дают одинаковый результат на простом массиве"""
    arr = [4, 2, 8, 1, 5]

    bubble_result = bubble_sort(arr)
    selection_result = selection_sort(arr)
    heap_result = heap_sort(arr)
    python_result = python_sort(arr)

    # Все должны быть равны
    assert bubble_result == selection_result == heap_result == python_result
    assert heap_result == [1, 2, 4, 5, 8]

def test_all_three_sorts_same_result_random():
    """Тестируем на случайных массивах разного размера"""
    for size in [5, 10, 15, 20, 25]:
        arr = [random.randint(1, 100) for _ in range(size)]

        bubble_result = bubble_sort(arr)
        selection_result = selection_sort(arr)
        heap_result = heap_sort(arr)
        python_result = python_sort(arr)

        # Проверяем что все результаты одинаковые
        assert bubble_result == selection_result == heap_result == python_result

        # И что результат отсортирован
        for i in range(len(bubble_result) - 1):
            assert bubble_result[i] <= bubble_result[i + 1]

# 2. Свойство: идемпотентность всех трёх сортировок

def test_idempotence_all_three():
    """Все три сортировки идемпотентны"""
    arr = [random.randint(1, 50) for _ in range(10)]

    # Тестируем каждую сортировку
    for sort_func in [bubble_sort, selection_sort, heap_sort]:
        first_sort = sort_func(arr)
        second_sort = sort_func(first_sort)

        # Должны получить тот же результат
        assert first_sort == second_sort, f"Сортировка {sort_func.__name__} не идемпотентна"

def test_idempotence_cross_check():
    """Перекрёстная проверка идемпотентности"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]

    bubble_once = bubble_sort(arr)
    bubble_twice = bubble_sort(bubble_once)

    selection_once = selection_sort(arr)
    selection_twice = selection_sort(selection_once)

    heap_once = heap_sort(arr)
    heap_twice = heap_sort(heap_once)

    # Все должны быть равны после повторной сортировки
    assert bubble_once == bubble_twice
    assert selection_once == selection_twice
    assert heap_once == heap_twice
    assert bubble_once == selection_once == heap_once

# 3. Свойство: сохранение элементов во всех трёх сортировках

def test_preserves_all_elements_all_three():
    """Все три сортировки сохраняют все элементы"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    bubble_result = bubble_sort(arr)
    selection_result = selection_sort(arr)
    heap_result = heap_sort(arr)

    # Проверяем что все содержат одинаковые элементы
    assert set(arr) == set(bubble_result) == set(selection_result) == set(heap_result)
    assert len(arr) == len(bubble_result) == len(selection_result) == len(heap_result)

    # Проверяем количество каждого элемента
    for num in set(arr):
        original_count = arr.count(num)
        assert original_count == bubble_result.count(num)
        assert original_count == selection_result.count(num)
        assert original_count == heap_result.count(num)

# 4. Свойство: работа с разными типами данных

def test_negative_numbers_all_three():
    """Все три сортировки работают с отрицательными числами"""
    arr = [-3, -1, -5, 0, 2, -2, 7, -8, 4, -1]

    bubble_result = bubble_sort(arr)
    selection_result = selection_sort(arr)
    heap_result = heap_sort(arr)
    python_result = python_sort(arr)

    expected = [-8, -5, -3, -2, -1, -1, 0, 2, 4, 7]

    assert bubble_result == expected
    assert selection_result == expected
    assert heap_result == expected
    assert python_result == expected

def test_duplicates_all_three():
    """Все три сортировки корректно обрабатывают дубликаты"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 1]

    bubble_result = bubble_sort(arr)
    selection_result = selection_sort(arr)
    heap_result = heap_sort(arr)

    # Все должны дать одинаковый результат с дубликатами
    assert bubble_result == selection_result == heap_result

    # Проверяем что дубликаты на месте
    assert bubble_result.count(1) == 3
    assert bubble_result.count(3) == 2
    assert bubble_result.count(5) == 3





