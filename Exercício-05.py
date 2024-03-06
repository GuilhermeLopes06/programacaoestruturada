def média(n1,n2,n3):
    m = (n1+n2+n3)/3
    if m < 0 or m > 10:
        print("Número inválido")
    elif m == 10:
        print("Aprovado com Distinção")
    elif m >= 7:
        print ("Aprovado")
    else:
        print ("Reprovado")

def main():
    (média(10,10,10))

main()