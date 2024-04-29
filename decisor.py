from numeros.operacoes import arit, exp
# from .operacoes import arit, exp

def selecionar_operacao(n1,n2,oper):

    match oper:
        case "+":
            print(arit.soma(n1,n2))
        case "-":
            print(arit.sub(n1,n2))
        case "x":
            print(arit.mult(n1,n2))
        case "/":
            print(arit.div(n1,n2))
        case "^":
            print(exp.potencia(n1,n2))
        case "#":
            print(exp.raiz(n1,n2))