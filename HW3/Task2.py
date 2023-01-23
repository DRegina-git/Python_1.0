# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample


def list_create_num(count):
    list_num = sample(range(1, count * 2), count)
    return list_num

def mult_nums(list_num):
        result_list = []
        
        for k in range(len(list_num) // 2):
            result_list.append(list_num[k] * list_num[len(list_num) - k - 1])
        if len(list_num) % 2:
            result_list.append(list_num[len(list_num) // 2])
        return result_list
numbers_list = list_create_num(int(input('Enter number: ')))
print(numbers_list)
print(mult_nums(numbers_list))
