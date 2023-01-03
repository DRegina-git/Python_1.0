# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
x1 = int(input('Enter the coordinates of the first point along the axis x: '))
y1 = int(input('Enter the coordinates of the first point along the axis y: '))
z1 = int(input('Enter the coordinates of the first point along the axis z: '))
x2 = int(input('Enter the coordinates of the second point along the axis x: '))
y2 = int(input('Enter the coordinates of the second point along the axis y: '))
z2 = int(input('Enter the coordinates of the second point along the axis z: '))
print(f'{((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5:0.4}')
