"""
Dicionários:
- Imutáveis
- Desordenados
- Únicos
-Consigo acessar diretamente um elemento, a partir de sua chave

"""

conj = {"uva", "banana", "morango", "uva", "uva" }
print(conj)
for fruta in conj:
    print(fruta)

print("banana" in conj)

lista = [2,3,5,3,2,3,1,7,5,3]
lista = list(set(lista))
print(lista)

alunos = ["zé", "ana", "álvaro"]
notas = [7.5, 8.2, 3.4]
cursos = ["EC", "ES", "CD"]

# {chave: valor}
alunos = {
    "zé": [7.5, "EC"],
    "ana": [8.2, "ES"],
    "álvaro": [3.4, "CD"]

}

#Método get retorna NONE caso a chave não exista
print(alunos.get("victor"))
print(alunos.get("victor", "Erro! Nome não encontrado"))

alunos = [
    {
        "nome": "ana",
        "nota": 8.3,
        "curso": "ES"
    }
]

print(alunos[0]["nome"])
print(alunos[0]["nota"])
print(alunos[0]["curso"])

for chave in alunos[0].keys():
    print(chave)
print("-" * 30)

print("-" * 30)

def op1():
    print("opção 1")

def op2():
    print("opção 2")

def op3():
    print("opçao 3")

def erro():
    print("impossível")


opcoes = {
    "1": op1,
    "2": op2,
    "3": op3
}

def main():
    while True:
        print("1 - Opção 1")
        print("2 - Opção 2")
        print("3 - Opção 3")
        opcao = input("Informe a opção: ")
        opcoes.get(opcao, erro)()

main()