#nao utilizar estrutura condicional
#nao utilizar bibliotecas

#quantidade máxima de diamantes, para encontrar o máximo entre 2 valores:
#x = (a + b + (|a - b|)) / 2.

a = int(input())
b = int(input())
c = int(input())
h = int(input())

#qnt MEDIA de diamente dos meninos
artur_pedro = (a + b + abs(a - b)) / 2
#qtd maxima de diamante
luiz = ((artur_pedro + c + abs(artur_pedro - c)) / 2) * h
print(int(luiz))