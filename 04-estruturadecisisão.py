"""
Programção estruturada

Estrutura de decisão (ou seleção)
- if/elif/else
-match/case

"""

def saudacao(turno):
    if turno == "M":
        print("Bom dia!")
    elif turno == "T":
        print("Boa tarde!")
    elif turno == "N":
        print("Boa noite!")
    else:
        print("Informação inválida!")
saudacao("T")
saudacao("N")
saudacao("M")
saudacao("A")

def saudacao2(turno): #Toda função se encerra no return, portanto nessse caso nao precisa de else
    if turno == "M":
        return "Bom dia!"
    if turno == "T":
        return "Boa tarde!"
    if turno == "N":
        return "Boa noite!"
    return "Informação inválida"

#Ternários
def e_par(num):
   return "é par" if num % 2 == 0 else "é ímpar"

print(e_par(10))

def e_par2(num):
    return num % 2 == 0

print(e_par2(5))

def le_nome():
    nome = input("Informe seu nome: ")
    if nome == "":
        print("Nome inválido!")

    #Usar dessa forma é mais comum, "" é igual a False
    if not nome:
        print("Nome ínvalido!")


    return nome

def avaliação(conceito):
    match conceito:
        case "bom":
            print("Aprovado")
        case "ótimo":
            print("Aprovado")
        case "Excelente":
            print("Aprovado")
        case _: #default case, opcional
            print("reprovado")

def avaliacao3(conceito):
    match conceito:
        case "Bom" | "Ótimo" | "Excelente":
            print ( "Aprovado")
        case _:
            print("Reprovado")

