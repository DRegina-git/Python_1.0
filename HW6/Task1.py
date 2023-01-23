# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

from random import sample

def larger_num(nums):
    new_list = sample(range(100), nums)
    print(new_list)
    return[new_list[nums] for nums in range(1, len(new_list)) if new_list[nums] > new_list[nums - 1]]

print(larger_num(int(input('Enter number: '))))