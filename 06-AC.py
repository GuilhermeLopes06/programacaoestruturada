#Exercício 1: Hello World
print("Hello World!")

#Exercício 2: Extremely basic
a = int(input())
b = int(input())
x = a + b
print("X =",x)

#Exercício 3: Simple calculate
total = 0
for i in range(2):
    item = input().split(" ")
    #item = [13] [2] [15.30]
    cod = int(item[0])
    qt = int(item[1])
    valor = float(item[2])
    total = total + qt*valor
print("VALOR A PAGAR: R$ %.2f" %total)

#Exercício 4: The greatest
num = input().split(" ")
a = int(num[0])
b = int(num[1])
c = int(num[2])
maior = max(a,b,c)
print(maior,"eh o maior")

#Exercício 5: Distance between two points
p1 = input().split(" ")
p2 = input().split(" ")

x1 = round(float(p1[0]),2)
y1 = round(float(p1[1]),2)

x2 = round(float(p2[0]),2)
y2 = round(float(p2[1]),2)

distancia = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 4)
print(distancia)