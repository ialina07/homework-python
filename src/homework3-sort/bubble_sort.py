def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

d = []
size = int(input('введите размер массива '))
for i in range(size):
    x = int(input('введите элемент массива '))
    d.append(x)

print(bubble_sort(d))
