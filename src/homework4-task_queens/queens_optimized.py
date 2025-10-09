def n_queens_bitmask(n):
    """Самое быстрое решение с использованием битовых масок"""
    if n < 1:
        return 0

    def backtrack(row=0, columns=0, diagonals1=0, diagonals2=0):
        if row == n:
            return 1

        count = 0
        # Доступные позиции в текущей строке
        available_positions = ((1 << n) - 1) & ~(columns | diagonals1 | diagonals2)

        while available_positions:
            # Берем самую правую доступную позицию
            position = available_positions & -available_positions
            # Убираем ее из доступных
            available_positions -= position

            count += backtrack(
                row + 1,
                columns | position,
                (diagonals1 | position) << 1,
                (diagonals2 | position) >> 1,
            )

        return count

    return backtrack()


def test_bitmask_basic():
    """Тест оптимизированного решения (bitmask)"""
    print("ТЕСТИРОВАНИЕ BITMASK РЕШЕНИЯ")
    print("=" * 50)

    # Известные значения для N ферзей
    test_cases = [
        (1, 1),  # [0]
        (2, 0),  # нет решений
        (3, 0),  # нет решений
        (4, 2),  # 2 решения
        (5, 10),  # 10 решений
        (6, 4),  # 4 решения
        (7, 40),  # 40 решений
        (8, 92),  # 92 решения
        (9, 352),  # 352 решения
        (10, 724),  # 724 решения
    ]

    all_passed = True

    for n, expected in test_cases:
        result = n_queens_bitmask(n)

        if result == expected:
            print(f"✓ N={n}: {result} (ожидалось {expected})")
        else:
            print(f"✗ N={n}: {result} (ожидалось {expected})")
            all_passed = False

    print("=" * 50)
    print(f"РЕЗУЛЬТАТ: {'Все тесты пройдены' if all_passed else 'Есть ошибки'}")

    return all_passed


# Запуск теста
if __name__ == "__main__":
    test_bitmask_basic()
