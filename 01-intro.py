
# comntário
# on interprtador igora tudo que está á direit do

"""
Docstrings

Comenário de várias linhas:

Introdução a python:
-Comentários
-Exibição de dados na tela
-Tipos de dados
-Leitura de dados
-Variáveis
-Alterações de tipos

"""

print('Olá mundo', end='\n')
print('olá', 'Mundo', sep="--")

"""

Tipos de dados em python
    int
    floar
    str
    bool( False=0 e True=1)  #bool - 1bit

"""

print("""Representação
 de um texto""")# 3 Aspas duplas para textos grandes em várias linhas

# esape char - \
print("Meu nome é \"guilherme\"\n lopes")
print("texto \\novo")
print("texto \t deslocado")

print(input("informe o seu nome: "))

#None
print(print("olá, mundo"))

#O resultado do input é sempre uma str


nome = input('Informe o seu nome: ')
print('Olá', nome)

# Python é uma linguagem de tipagem fraca e dinâmica

# Type hint
idade : int = 16

# Python não possui o conceito de constante


print(type("2"))
print(type(int("2")))
print(type(2))

# Todo dado diferente de 0, 0.0, "", etc. são considerados como True