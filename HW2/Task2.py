# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
n = int(input())
m = 1
n_list = []
for i in range(1, n + 1):
    m*= i
    n_list.append(m)
print(n_list)