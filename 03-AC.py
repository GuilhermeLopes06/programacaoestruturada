#Exercício 1:
def determina_tipo_triangulo(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return "Não é um triângulo"
    elif a == b and a == c:
        return "Equilátero"
    elif a ==  b or b == c or a == c:
        return "Isóceles"
    return "Escaleno"
def main():
    print(determina_tipo_triangulo(4,4,4))
    print(determina_tipo_triangulo(2,4,4))
    print(determina_tipo_triangulo(3,4,5))
    print(determina_tipo_triangulo(1,1,4))
main()


#Exercício 2:
def testa_dia_semana(n):
    match n:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-Feira"
        case 3:
            return "Terça-Feira"
        case 4:
            return "Quarta-Feira"
        case 5:
            return "Quinta-Feira"
        case 6:
            return "Sexta-Feira"
        case 7:
            return "Sábado"
    return ""
def main():
    print(testa_dia_semana(2))
    print(testa_dia_semana(6))
    print(testa_dia_semana(7))
    print(testa_dia_semana(9))
main()


#Exercício 3:
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

def leitura():
    n1 = int(input("Informe um número: "))
    n2 = int(input("Informe outro número: "))
    operacao = input("Informe a operação: ").upper()
    return n1,n2,operacao

def main():
    n1, n2, operacao = leitura()
    match operacao:
        case "SOMA":
            print(soma(n1, n2))
        case "SUBTRAÇÃO":
            print(subtracao(n1, n2))
        case "MULTIPLICAÇÃO":
            print(multiplicacao(n1, n2))
        case "DIVISÃO":
            print(divisao(n1, n2))
        case _:
            print("Operação inválida")
main()