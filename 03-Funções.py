"""

Funções:
- Evitar duplicidade de código
- Organizar o código

Princípios Solid:
SRP - Single Responsability Principle

Encapsulamento

"""

def traco(largura,caract_traco):
    print(caract_traco * largura)




# def -> definir (ou declarar), Definir variáveis e seus padrões
def cabecalho(título, largura=30, caract_traco ="-"):
    traco(largura, caract_traco)
    print(título)
    traco(largura, caract_traco)

# Chamada da função
cabecalho("Relaório de vendas", largura=30, caract_traco="_")
cabecalho("Folha de pagamento", largura=25, caract_traco=".")
cabecalho("lista de fornecedores", caract_traco=">-<")

"""
Entrada de dados
processamento
Saída de dados

"""

def soma(a,b):
    return a + b #Estabelece o retorno da função

print (soma (546, 1009) + (45762 +26387))

def e_par(num):
    return num % 2 == 0

def subsequentes (num):
    return num + 1, num + 2 # A função retorna uma tupla

x,y = subsequentes(10)
print(x,y)
print("--"*30)
#Escopo de variáveis
x=0 #escopo global

def func1(x):
    x = 1 #escopo local
    print(x)

def func2():
    x = 2
    print(x)

def func3():
    print(x)

def func4():
    global x #Não usar!!!
    x = 4
    print(x)


print(x)
func1(x)
func2()
func3()
func4()
print(x)

# Evitar o uso de variáveis globais
# A não ser que sejam constantes (no início do arquivo)
