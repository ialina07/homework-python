def evkl(a, b):
    if a == 0:
        return b, 0, 1
    else:
        nod, x, y= evkl(b%a, a)
        return nod, y-(b//a)*x, x
a = int(input())
b = int(input())
nod, x, y = evkl(a, b)
print(f'НОД({a}, {b}) = {nod}')
print(f'линейная комбинация: {a}*{x} + {b}*{y} = {nod}')
