""" 
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""
def which_dots(var):
    if var=='1':
        return ['(0;infinity)','(0;infinity)']
    elif var=='2':
        return ['(-infinity;0)','(0;infinity)']
    elif var=='3':
        return ['(-infinity;0)','(-infinity;0)']   
    elif var=='4':
        return ['(0;infinity)','(-infinity;0)'] 

s=input('Введите номер четверти: ')
a=which_dots(s)
print(f'{s}-й четверти плоскости принадлежит множество точек по оси х в диапазоне {a[0]},по оси y в диапазоне {a[1]}')