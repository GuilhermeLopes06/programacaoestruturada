#EXERCÍCIO 1:
aux=False
while True:
    n=int(input())
    if n==0:break
    dados = dict()
    for i in range(n):
        nome=input()
        x=input().split()
        x.append(nome)
        dados[i]=x
    dados=dict(sorted(dados.items(),key=lambda x: x[1][2]))
    dados=dict(sorted(dados.items(),key=lambda x: x[1][1],reverse=True))
    dados=dict(sorted(dados.items(),key=lambda x: x[1][0]))
    if aux:
        print()
    for i,j in dados.items():
        print(*j,sep=" ")
    aux=True

#EXERCÍCIO 2:
n = int(input())
all_strings = []

for i in range(n):
    arvores = []  
    while True:
        arvore = input()
        if arvore == "":
                    break
        arvores.append(arvore)
        if i == n-1:
            try:  
                arvore = input()
            except EOFError:
                break

    total = len(arvores)
    aux = sorted(set(arvores))
    strings = []
  
    for especie in aux:
        porcentagem = (arvores.count(especie) / total) * 100
        strings.append("{} {:.4f}".format(especie, porcentagem))
    all_strings.append(strings)
    
for strings in all_strings:
    for string in strings:
        print(string)
    print()


#EXERCÍCIO 3:
import math
while True:
    try: 

        n = int(input())
        medadosidadosas = input().split(" ")
        h = int(medadosidadosas[0])/100
        c = int(medadosidadosas[1])/100
        l = int(medadosidadosas[2])/100
        hip = math.sqrt((h**2)+(c**2))
        area = hip*l*n
        print(f"{area:.4f}")
    
    except EOFError:
        break
