"""
Baskhara

"""
a = int(input("Informe o parâmetro a da equação: "))
b = int(input("Informe o parâmetro b da equação: "))
c = int(input("Informe o parâmetro c da equação: "))
delta = b**2 - 4*a*c 
raiz1 = (-b + delta**0.5)/2**a 
raiz2 = (-b - delta**0.5)/2**a 
print("A primeira raíz da equação é ",raiz1)
print("A segunda raíz da equação é ",raiz2)

"""

Ano bissexto

"""


ano = int(input("Informe o ano: "))
print(ano%4 == 0 and ano%100 != 0 or ano%400 == 0 and ano%100 == 0) #Dessa forma são separados os anos bissextos múltiplos e não múltiplos de 100