"""
Tratamento de erros e exceções:
- try / except / else / finally

"""

def divisao(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Erro! Divisão por zero")
    except TypeError:
        print("Erro! Os tipos são incompatíveis")
    except Exception as erro:
        print(f"Erro do tipo {type(erro).__name__}: {erro}")

divisao(12,0) #ZeroDivisionError
divisao("a", 2) #TypeError


def terceira_letra():
    nome = input()
    try:
        print(f"A terceira letra é {nome[2]}.")
    except IndexError:
        print("O nome precisa ter mais de das letras")
    else: # entra se n surgiu uma exeção
        print("Leitura feita com sucesso")
    finally: #entra sempre (encerra operações)
        print("Fim do try")

#terceira_letra()

def divisao2(a,b):
    if b == 0:
        raise ValueError

#divisao2(2,0)

def func1():
    raise NotImplementedError

def func2():
    raise NotImplementedError

def func3():
    raise NotImplementedError

class TamanhoExcedidError(Exception):
    pass


lista = [1,2,3,4,5]

if len(lista) > 4:
    raise TamanhoExcedidError