# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

from random import sample

def mult_num(nums):
    return[nums for nums in range(20, nums + 1) if nums % 20 == 0 or nums % 21 == 0]

print(mult_num(int(input('Enter number: '))))