# other_sorts.py

def bubble_sort(arr):
    """
    Пузырьковая сортировка
    """
    if not arr:
        return arr.copy()

    arr = arr.copy()  # Работаем с копией, чтобы не менять оригинал
    n = len(arr)

    # Проходим по массиву n раз
    for i in range(n):
        # Сравниваем соседние элементы
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем местами, если нужно
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def selection_sort(arr):
    """
    Сортировка выбором - ищем минимальный элемент и ставим на правильное место
    """
    if not arr:
        return arr.copy()

    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        # Предполагаем, что текущий элемент - минимальный
        min_index = i

        # Ищем настоящий минимальный элемент в оставшейся части
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Меняем местами с текущим элементом
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Встроенная сортировка Python для сравнения
def python_sort(arr):
    """Используем встроенную сортировку как эталон"""
    return sorted(arr.copy())
