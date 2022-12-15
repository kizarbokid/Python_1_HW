""" 
Напишите программу для. проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

"""
print('Если все переменные True:')
x,y,z=True,True,True
print('1)¬(X ⋁ Y ⋁ Z) = ',not(x and y and z) )
print('2)¬X ⋀ ¬Y ⋀ ¬Z = ',not(x) or not(y) or not(z))
print('Следовательно, ',not(x and y and z),' = ',not(x) or not(y) or not(z))

print('Если все переменные False:')
x,y,z=False,False,False
print('1)¬(X ⋁ Y ⋁ Z) = ',not(x and y and z) )
print('2)¬X ⋀ ¬Y ⋀ ¬Z = ',not(x) or not(y) or not(z))
print('Следовательно, ',not(x and y and z),' = ',not(x) or not(y) or not(z))

print('Если 1 отличается:')
x,y,z=True,False,True
print('1)¬(X ⋁ Y ⋁ Z) = ',not(x and y and z) )
print('2)¬X ⋀ ¬Y ⋀ ¬Z = ',not(x) or not(y) or not(z))
print('Следовательно, ',not(x and y and z),' = ',not(x) or not(y) or not(z))