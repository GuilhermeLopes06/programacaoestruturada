n = int(input())
all_strings = []

for _ in range(n):
    arvores = []  
    while True:
        try:
                tree = input()
                if tree == "":
                    break
                arvores.append(tree)
        except EOFError:
                    break
        

    total = len(arvores)
    aux = sorted(set(arvores))
    strings = []
  

    for especie in aux:
        porcentagem = (arvores.count(especie) / total) * 100
        strings.append("{} {:.4f}".format(especie, porcentagem))
    all_strings.append(strings)

for k in all_strings:
    for strings in k:
        print(strings)
    print()