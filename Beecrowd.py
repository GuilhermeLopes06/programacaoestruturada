#EXERCÍCIO 1:
salario = round(float(input()),2)
if salario >= 0 and salario <= 400.00:
    print(f"Novo salario: {salario*1.15:.2f}")
    print(f"Reajuste ganho: {salario*0.15:.2f}")
    print("Em percentual: 15 %")
elif salario >= 400.01 and salario <= 800.00: 
    print(f"Novo salario: {salario*1.12:.2f}")
    print(f"Reajuste ganho: {salario*0.12:.2f}")
    print("Em percentual: 12 %")
elif salario >= 800.01 and salario <= 1200.00:
    print(f"Novo salario: {salario*1.1:.2f}")
    print(f"Reajuste ganho: {salario*0.1:.2f}")
    print("Em percentual: 10 %")
elif salario >= 1200.01 and salario <= 2000.00:
    print(f"Novo salario: {salario*1.07:.2f}")
    print(f"Reajuste ganho: {salario*0.07:.2f}")
    print("Em percentual: 7 %")
else:
    print(f"Novo salario: {salario*1.04:.2f}")
    print(f"Reajuste ganho: {salario*0.04:.2f}")
    print("Em percentual: 4 %")

#EXERCÍCIO 2:
numeros = []
pares = 0
for c in range(5):
    n = int(input())
    numeros.append(n)

for i in numeros:
    if i % 2 == 0:
        pares += 1

print(f"{pares} valores pares")

#EXERCÍCIO 3:
soma = 0
x = int(input())
y = int(input())
if x<y:
    for i in range(x, y+1):
        if i % 13 != 0:
            soma += i
else:
    for i in range(y, x+1):
        if i % 13 != 0:
            soma += i

print(soma)

#EXERCÍCIO 4:
v = 51
while v > 50:
    v = int(input())
print(f"N[0] = {v}")
for c in range(1,10):
    v *= 2
    print(f"N[{c}] = {v}")

#EXERCÍCIO 5:
n = 1001
while n < 1 or n > 1000:
    n = int(input())

num_lista = input()
x = num_lista.split(" ")

menor = int(x[0])
pos = 0

for c in range (0,n):
    x[c] = int(x[c])
    if x[c] < menor:
        menor = x[c]
        pos = c

print(f"Menor valor: {menor}")
print(f"Posicao: {pos}")

#EXERCÍCIO 6:
coluna = int(input())
operacao = input()
   

m=[]
for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x)
        

if operacao == 'S':
    soma = 0
    for k in range(12):
        soma += m[k][coluna]
    print(soma)
if operacao == 'M':
    med = 0
    soma = 0
    for k in range(12):
        soma = soma + m[k][coluna]
    med= soma/12
    print(f"{med:.1f}")

#EXERCÍCIO 7:
n = int(input())
while n > 0:
    n -= 1
    c = input().split()
    c.sort(key=len, reverse=True)
    for i in range(len(c)):
        print(c[i], end = '')
        if i != len(c)-1:
            print(' ', end = '')
    print()