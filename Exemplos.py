"""

Receba vlores ->parametrôs
leia valores -> input


"""
def leitura():
    a = float(input("Informe um número: "))
    b = float(input("Informe outro número: "))
    return a, b

def soma(a, b):
    return a+b

def subtração(a, b):
    return a - b

def main():
    a, b = leitura()
    print("A soma é", soma(a, b), "e a subtração é", subtração(a, b))
main()