# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
i = int(input())
if i == 1:
    print('x > 0 and y > 0')
elif i == 2:
    print('x < 0 and y > 0')
elif i == 3:
    print('x < 0 and y < 0')
elif i == 4:
    print('x > 0 and y < 0')
else:
    print('Such quarter is not found')