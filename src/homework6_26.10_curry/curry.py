def curry(func, arity):
    #проверка корректности арности
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Арность должна быть целым неотрицательным числом")

    def curried(*args):
        if len(args) >= arity:
            return func(*args[:arity])
        else:
            def partial(*more_args):
                return curried(*(args + more_args))
            return partial

    return curried

def uncurry(curried_func, arity):
    #проверка корректности арности
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Арность должна быть целым неотрицательным числом")

    def uncurried(*args):
        if len(args) != arity:
            raise ValueError(f"Ожидалось {arity} аргументов, получено {len(args)} аргументов")

        result = curried_func
        for i in range(arity):
            if not callable(result):
                raise ValueError("Функция каррирования была применена слишком много раз")
            result = result(args[i])

        if callable(result):
            raise ValueError("Функция каррирования была применена недостаточно раз")

        return result

    return uncurried

#тестовый пример
def sum3(x, y, z):
    return x + y + z

sum3_curry = curry(sum3, 3)
sum3_uncurry = uncurry(sum3_curry, 3)
print(sum3_curry(1)(2)(3))    # 6
print(sum3_uncurry(1, 2, 3))  # 6
