""" 
    Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
    выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
"""
def which_quarter(x,y):
    if x>0 and y>0:
        return "I"
    elif x<0 and y>0:
        return "II"
    elif x<0 and y<0:
        return "III"
    else:
        return "IV"

s=input('Введите координаты точки на плоскости (через пробел): ')
coordinates=[int(s) for s in s.split()]
print(f'Точка принадлежит {which_quarter(coordinates[0],coordinates[1])} четверти')