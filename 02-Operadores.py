"""
Aula 2

Opeadores
- Aritméticos
- atribução
- Comparação (ou Realcionais)
- Lógicos (ou booleanos)

"""

# Operadores aritméticos
#Quando ambos os operandos são números

x = 10
y = 5

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y) # arredonda pra baixo
print(x%y)
print(x**y)
print(round(x + y, 1))

# r + q.d = D

# Quando um dos operandos for uma str:

print("-" * 30)
print("-" + "+")

# Operadore de atribuição

x = 2
x += 1 # x = x+1
x -= 4 #x = x-4


#A partir daquia é bem incomum usar
x*= 6 #
x/= 2
x //= 4
x **= 2
x%= 5
print(x)

x *= 10
print(x)

# Operadores de comparação
# Sempre vão retornar um booleano

print( "-" * 30)
print ( x>y)
print(x<y)
print( x==y)
print(  x!=y)

z = "abc"
w = "Abc"

print( "-"*30)
print( z > w) # tabela ASCI ou número de caracteres
print( z < w)
print( z==w)
print( z != w)

# Operadores lógicos

a = True
b = False

print("-" * 30)
print( a and b )
print(a or b)
print(not a)

# Type casting
idade = int(input("Informe sua idade:"))
print("sua idade é " + str(idade))

print(bool(""))
print(bool(0))
print(bool(0.0)) #Valor do False
print(bool("10"))
print(bool(12.5))
print(bool(1))

print("" or 0.0)
print("10" or 75) #Retorna o primeiro valor verdadeiro

print(True and False ) # Se o primeiro for falso ele é retornado, já se for verdadeiro o segundo é retornado


nome = input("Informe seu nome: ") or "Nome inválido"


print(nome)
print("-" *30)

"""

Ordem de precedência:

()
**
* / // %
+ -
Comparações
"""