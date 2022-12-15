""" 
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
"""
import math
def pifagor(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

s=input('Введите координаты точек на плоскости (через пробел): ')
coord=[float(s) for s in s.split()]
dist=pifagor(coord[0],coord[1],coord[2],coord[3])
print(f'Расстояние между {coord[0],coord[1]} и {coord[2],coord[3]} составляет ',round(dist,2))