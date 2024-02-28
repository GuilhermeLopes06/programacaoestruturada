maiores = 0
menores = 0
for c in range (1,11):
    date = int(input('Qual é a idade da {} pessoa'.format(c)))
    if (2024-date) >= 18:
        maiores += 1
    else:
        menores +=1
print("Neste grupo {} são de maior e {} sao de menor".format(maiores,menores))



