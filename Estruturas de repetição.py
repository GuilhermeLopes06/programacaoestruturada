"""
While -> Não sabemos qunatas vezes vamos executar a repetição
For -> Quando queremos acessar todos os elementos de uma coleção de dados
"""
def contagem_regressiva(num):
    while num >= 0:
        print(num)
        num -= 1

contagem_regressiva(5)
print("-=" * 30)

#Evitar loops infinitos
def contagem_regresiva3(num):
    for c in range(num, -1, -1): #(start,stop,step)
        print(c)


contagem_regresiva3(4)
print("-=" * 30)

def ola_varias_vezes(num):
    for c in range(num): #c = _
        print("Olá")

ola_varias_vezes(10)
print("-=" * 30)

def le_nomes():
    texto = "1"
    while texto != "":
        texto = input("Informe um texto ou búemro: ")
        if texto.isnumeric():
            continue #Interrompe o loope atual
        print(texto)
#

def le_nome():
    while True:
        nome = input("Informe o seu nome: ")
        if nome:
            break
    print(nome)