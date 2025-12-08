def is_valid_recursive(board, row, col):
    """Проверяет, можно ли поставить ферзя на позицию (row, col)"""
    # Проверяем все предыдущие строки
    for i in range(row):
        # Проверка по вертикали и диагоналям
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens_recursive(n, row=0, board=None, count=None):
    """Рекурсивное решение с backtracking"""
    if board is None:
        board = [-1] * n
    if count is None:
        count = [0]

    if row == n:
        # Найдена корректная расстановка
        count[0] += 1
        return

    for col in range(n):
        if is_valid_recursive(board, row, col):
            board[row] = col
            solve_n_queens_recursive(n, row + 1, board, count)
            # Backtrack - не нужно явно сбрасывать, так как перезаписываем

    return count[0]


def n_queens_recursive(n):
    """Обертка для рекурсивного решения"""
    if n < 1:
        return 0
    return solve_n_queens_recursive(n)


def test_n_queens_recursive_basic():
    """Тест рекурсивного решения на известных значениях"""
    print("ТЕСТИРОВАНИЕ РЕКУРСИВНОГО РЕШЕНИЯ")
    print("=" * 40)

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
    ]

    all_passed = True

    for n, expected in test_cases:
        result = n_queens_recursive(n)

        if result == expected:
            print(f"✓ N={n}: {result} (ожидалось {expected})")
        else:
            print(f"✗ N={n}: {result} (ожидалось {expected})")
            all_passed = False

    print("=" * 40)
    print(f"РЕЗУЛЬТАТ: {'Все тесты пройдены' if all_passed else 'Есть ошибки'}")

    return all_passed


# Запуск теста
if __name__ == "__main__":
    test_n_queens_recursive_basic()
