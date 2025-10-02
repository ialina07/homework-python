#include <stdio.h>

//объявление ассемблерной функции
extern int bubble_sort_asm(int* array, int count);

int main()
{
    int numbers[100];
    int count = 0;

    //чтение чисел из стандартного ввода
    while (scanf("%d", &numbers[count]) == 1 && count < 100) {
        count++;
    }

    //вызов ассемблерной функции сортировки
    int changed_count = bubble_sort_asm(numbers, count);

    //вывод отсортированного массива
    for (int i = 0; i < count; i++) {
        printf("%d", numbers[i]);
    }
    printf("\n");

    //возвращаем количество перемещенных элементов
    return changed_count;
}
