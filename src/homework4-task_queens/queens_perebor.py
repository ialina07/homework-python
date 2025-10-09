import itertools


def is_valid_placement(positions):
    """Проверяет, является ли расстановка ферзей корректной"""
    n = len(positions)
    for i in range(n):
        for j in range(i + 1, n):
            # Проверка на одну строку (невозможно в нашей модели)
            # Проверка на одну диагональ
            if abs(positions[i] - positions[j]) == abs(i - j):
                return False
    return True


def n_queens_placement(n):
    """Перебор всех возможных расстановок"""
    if n < 1 or n > 10:  # Ограничение для перебора
        return 0

    count = 0
    # Генерируем все перестановки (каждый ферзь в своем столбце)
    for permutation in itertools.permutations(range(n)):
        if is_valid_placement(permutation):
            count += 1
    return count


def test_placement_small():
    """Тестирование для маленьких N где перебор работает быстро"""
    test_cases = {
        1: 1,  # [0]
        2: 0,  # нет решений
        3: 0,  # нет решений
        4: 2,  # [1,3,0,2] и [2,0,3,1]
        5: 10,  # известное значение
        6: 4,  # известное значение
    }

    print("Тестирование переборного решения:")
    print("N\tОжидаемо\tПолучено\tСтатус")
    print("-" * 40)

    for n, expected in test_cases.items():
        if n <= 6:  # Ограничиваем для скорости
            result = n_queens_placement(n)
            status = "✓" if result == expected else "✗"
            print(f"{n}\t{expected}\t\t{result}\t\t{status}")


if __name__ == "__main__":
    test_placement_small()
