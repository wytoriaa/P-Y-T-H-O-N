# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
# o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
# Após, calcule e mostre o valor a ser pago.

# Entrada
# O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, 
# respectivamente dois inteiros e um valor com 2 casas decimais.

# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, 
# lembrando de deixar um espaço após os dois pontos e um espaço após o "R$".
#  O valor deverá ser apresentado com 2 casas após o ponto.

peca1, numPeca1, valorPeca1 = input().split()
peca1 = int(peca1)
numPeca1 = int(numPeca1)
valorPeca1 = float(valorPeca1)

peca2, numPeca2, valorPeca2 = input().split()
peca2 = int(peca2)
numPeca2 = int(numPeca2)
valorPeca2 = float(valorPeca2)

calc = (numPeca1*valorPeca1) + (numPeca2*valorPeca2)
print("VALOR A PAGAR: R$ {:.2f}".format(calc))
