# Задайте список из n чисел, 
# заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
n = int(input())
m = 0
m_list = []
sum_n = 0
for i in range(1, n + 1):
    m = round((1 + 1/i) ** i, 4)
    m_list.append(m)
    sum_n +=m
print(m_list)
print(sum_n)