def ler_nome():
    """Retorna o nome do aluno"""
    return input("Qual é o seu nome? ")

def ler_notas():
    """Retorna as notas"""
    ap1 = float(input("Nota da AP1: "))
    ap2 = float(input("Nota da AP2: "))
    asub = float(input("Nota da AS: "))
    ac = float(input("Nota da AC: "))
    return ap1,ap2,asub,ac


def notas_sao_validas(ap1,ap2,asub,ac):
    """Retorna Tre se as notas rtão entre 0 e 10
        Retorna False caso cotrário
    """
    if 10 >= ap1 >= 0 and 10 >= ap2 >= 0 and 10 >= asub >= 0 and 10 >= ac >= 0:
        return True
    else:
        return False


def duas_maiores_notas(ap1,ap2,asub):
    """Retorna as duas maiores notas dentre as avaliações
    """
    if ap1 < asub and ap1 < ap2:
        return  asub,  ap2
    if ap2 < asub and ap2 < ap1:
        return asub, ap1
    if ap1 == ap2 and asub > ap1:
        return ap1, asub
    else:
        return ap1,ap2

def calcular_media(prova1,prova2,ac):
    """Retorna a média das avalições, arredondando para duas casas decimais
    MEDIA=(N1 + N2) * 0,4 + AC * 0,2
    """
    return (prova1 + prova2) * 0.4 + ac * 0.2

def aluno_foi_aprovado(media):
    return media >= 7


def main():
    nome = ler_nome()
    if nome: #(if nome True)
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1,ap2,asub,ac):
            prova1, prova2 = duas_maiores_notas(ap1, ap2, asub)
            media = round(calcular_media(prova1,prova2,ac), 2)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado!", media)
            else:
                print("Aluno foi reprovado", media)


main()



