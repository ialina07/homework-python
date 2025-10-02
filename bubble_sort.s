.section .note.GNU-stack,"",@progbits
.section .text
.global bubble_sort_asm

#функция: bubble_sort_asm
#параметры:
# rdi - указатель на массив
# rsi - количество элементов
возвращает:
# rax - количество элементов, изменивших положение

bubble_sort_asm:
    pushq %rbp
    movq %rsp, %rbp
    pushq %rbx
    pushq %r12
    pushq %r13
    pushq %r14

    #инициализация
    movq %rdi, %rbx    # rbx = указатель на массив
    movl %esi, %r12d   # r12d = количество элементов
    movl $0, %r13d     # r13d = счетчик измененных элементов

    #проверка на пустой массив или массив из одного элемента
    cmpl $1, %r12d
    jle .end_sort

    #внешний цикл (i)
    movl $0, %r14d    # r14d = i

.outer_loop:
    #проверка условия внешнего цикла
    movl %r12d, %eax
    decl %eax
    cmpl %r14d, %eax
    jle .end_sort

    #внутренний цикл (j)
    movl $0, %ecx    # ecx = j

.inner_loop:
    #вычисление индекса для внутреннего цикла
    movl %r12d, %eax
    subl %r14d, %eax
    decl %eax
    cmpl %ecx, %eax
    jle .end_inner_loop

    #загрузка array[j] и array[j+1]
    movl (%rbx, %rcx, 4), %edx      # edx = array[j]
    movl 4(%rbx, %rcx, 4), %eax     # eax = array[j + 1]

    #сравнение array[j] и array[j+1]
    cmpl %eax, %edx
    jle .no_swap

    #обмен элементов
    movl %eax, (%rbx, %rcx, 4)    #array[j] = array[j + 1]
    movl %edx, 4(%rbx, %rcx, 4)    #array[j + 1] = array[j]

    #увеличиваем счетчик измененных элементов
    incl %r13d

.no_swap:
    #следующая итерация внутреннего цикла
    incl %ecx
    jmp .inner_loop

.end_inner_loop:
    #следующая итерация внешнего цикла
    incl %r14d
    jmp .outer_loop

.end_sort:
    #возвращаем количество измененных элементов
    movl %r13d, %eax

    popq %r14
    popq %r13
    popq %r12
    popq %rbx
    popq %rbp
    ret
