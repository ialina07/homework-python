def exchange(coins, target_sum):
    """
    Функция для размена суммы target_sum с использованием монет из списка coins
    Возвращает список монет для размена или '-42!', если размен невозможен
    """
    # Создаем массив для хранения минимального количества монет для каждой суммы от 0 до target_sum
    min_coins = [float("inf")] * (target_sum + 1)
    min_coins[0] = 0

    # Заполняем массив min_coins для всех сумм от 1 до target_sum
    for i in range(1, target_sum + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Если для суммы target_sum не найдено решение
    if min_coins[target_sum] == float("inf"):
        return ("-42!")

    # Восстанавливаем конкретные монеты, используемые для размена
    res = []
    i = target_sum

    while i > 0:
        # Перебираем все монеты, чтобы найти, какая была использована
        for coin in coins:
            if min_coins[i] == min_coins[i - coin] + 1:
                res.append(coin)
                # Уменьшаем текущую сумму на номинал монеты
                i = i - coin
                break
    return res

coins = [5, 7, 10]  # Доступные номиналы монет
target_sum = int(input("Введите сумму для размена: ")) 

res = exchange(coins, target_sum)

print("размен числа", target_sum, "монетами:", res)
