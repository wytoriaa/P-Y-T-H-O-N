# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
#  A seguir, calcule e mostre o valor da conta a pagar.
# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)


precos = [4.00, 4.50, 5.00, 2.00, 1.50]
if (codigo == 1):
    valorTotal = quantidade * precos[0]
elif (codigo == 2):
    valorTotal = quantidade * precos[1]
elif (codigo == 3):
    valorTotal = quantidade * precos [2]
elif (codigo == 4):
    valorTotal = quantidade * precos [3]
elif (codigo == 5):
    valorTotal = quantidade * precos [4]

print(f"Total: R${valorTotal:.2f}")