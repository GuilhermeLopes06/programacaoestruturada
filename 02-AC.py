# Exercício 1: parte 1
def eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c
    return ((-b + delta**0.5)/2**a), ((-b - delta**0.5)/2**a)   
def main():
    print(eq_seg_grau(1, -6, 8))
main()

#Exercício 1: parte 2
def bissexto(ano):
    print(ano%4 == 0 and ano%100 != 0 or ano%400 == 0 and ano%100 == 0)
def main():
    bissexto(2012)
main()

#Exercício 2:
def calcula_salario(valor_hora, num_horas):
    irpf = 0.275
    return valor_hora * num_horas * (1 - irpf)
def main():
    print(calcula_salario(10, 220))
main()