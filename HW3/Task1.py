# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample


def list_create_num(count):
    list_num = sample(range(1, count * 2), count)
    return list_num


def sum_nums(list_num):
    n = 0
    for k in range(0, len(list_num), 2):
        n += list_num[k]
        return n


numbers_list = list_create_num(int(input('Enter number: ')))
print(numbers_list)
print(sum_nums(numbers_list))
