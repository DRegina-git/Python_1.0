# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def convert_num(num):
    list_num = []
    while num > 0:
        list_num.insert(0, num % 2)
        num //= 2
    print(list_num)
numbers_list = convert_num(int(input('Enter number: ')))
