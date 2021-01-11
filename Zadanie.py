#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу для решения задачи:
# В списке, состоящем из вещественных элементов, вычислить:
# 1) сумму положительных элементов списка;
# 2) произведение элементов списка, расположенных между максимальным
# по модулю и минимальным по модулю элементами.
# Упорядочить элементы списка по убыванию.

def cycle(resl=1):
    for j in A_new:
        resl *= j
    return resl


if __name__ == '__main__':
    A = list(map(float, input("Ввод: ").split()))
    res = 0

    # Первое задание
    for i in A:
        if i > 0:
            res += i
    print("1) ""%.2f" % res)

    # Второе задание
    L = []
    a_min = a_max = A[0]
    i_min = i_max = 0
    b = [abs(i) for i in A]
    for i, item in enumerate(b):
        if item < a_min:
            i_min, a_min = i, item
        if item >= a_max:
            i_max, a_max = i, item
    A_new = A[i_min + 1:i_max]

    res = cycle()
    if res == 1:
        A_new = A[i_max + 1:i_min]

        res = cycle()
    print(f"2) {res}")

    # Сортировка
    A.sort(reverse=True)
    print(f"3) {A} ")
