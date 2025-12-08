def heap_sort(arr):
    """
    Сортировка кучей
    """
    n = len(arr)

    # Строим кучу
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)

    # Извлекаем элементы
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Меняем корень с последним
        heap(arr, i, 0)  # Просеиваем новый корень

    return arr


def heap(arr, n, i):
    """
    Просеивание
    """
    largest = i  # Считаем текущий элемент наибольшим
    left = 2 * i + 1  # Левый ребенок
    right = 2 * i + 2  # Правый ребенок

    # Если левый ребенок существует и больше родителя
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый ребенок существует и больше наибольшего
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не родитель
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами
        heap(arr, n, largest)  # Просеиваем дальше
