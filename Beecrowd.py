#EXERCÍCIO 1:
distancia = int(input())
tempo = distancia*2
print(f"{tempo} minutos")

#EXERCÍCIO 2:
num = int(input())
n = 1
for i in range (2,num+1):
    n *= i
print(n)

#EXERCÍCIO 3:
n = int(input())
valores_a_pagar = []

for c in range(0,n):
    produtos = {
    "nomes": [],
    "precos": []
}
    conta = 0
    m = int(input())
    for i in range(0,m):
        dados = input().split(" ")
        produtos["nomes"].append(dados[0])
        produtos["precos"].append(dados[1])
    p = int(input())
    for x in range(0,p):
        prod = input().split(" ")
        y = produtos["nomes"].index(prod[0])
        conta += float(produtos["precos"][y])*float(prod[1])
    valores_a_pagar.append(conta)
for k in valores_a_pagar:
    print(f"R$ {k:.2f}")

#EXERCÍCIO 4:
n = input()
respotas = input().split(" ")
ganhadores = 0
for c in respotas:
    if c == n:
            ganhadores += 1
    else:
        pass
print(ganhadores)

#EXERCÍCIO 5:
dados = input().split(" ")
if int(dados[0]) * int(dados[2]) <= int(dados[1]):
    print("S")
else:
    print("N")

#EXERCÍCIO 6:
n = int(input())
total = 0
for c in range(0,n):
    dados = input().split(" ")
    dist = int(dados[0]) * int(dados[1])
    total += dist
print(total)

#EXERCÍCIO 7:
t = int(input())
print(t*4)

#EXERCÍCIO 8:
coluna = []
n = int(input())
while n < 3 and n > 500:
    n = int(input())
for i in range(0,n):
    num = int(input())
    while num != 1 and num != 2:
        num = int(input())
    coluna.append(num)

circulo = 0
num_ant = 0
for k in coluna:
    if k != num_ant:
        circulo += 1
        num_ant = k
    else:
        num_ant = k
        pass
print(circulo)

