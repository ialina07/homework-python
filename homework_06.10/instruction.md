# Компиляция C-файла
gcc -c main.c -o main.o

# Ассемблирование asm-файла  
as bubble_sort.s -o bubble_sort.o

# Линковка
gcc main.o bubble_sort.o -o sorter

# Запуск
echo "5 2 8 1 9" | ./sorter
echo "Количество элементов, изменивших свое положение: $?"
