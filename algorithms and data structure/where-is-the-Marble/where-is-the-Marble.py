#this question addresses binary Search and sort
#N = numero de marmores - N linhas conterão os numeros de escritos em cada um dos N marmores
#Q = numero de consultas - Q linhas conterao Q consultas
#A entrada termina qpor um caso de teste onde N e Q = 0
def busca_binaria(self, array, item, inicio, fim):
    if inicio <= fim:
        metade = (inicio + fim)//2
        if array[metade] == item:
            return metade
        if item < array[metade]:
            return busca_binaria(array, item, inicio, metade - 1)
        else:
           return busca_binaria(array, item, metade + 1 , fim)
    return None
def main():
    i = 0
    N, Q = input().split()
    N = int(N)
    Q = int(Q)
    if N and Q == 0:
        print('Fim do programa!')
    marble = []
    while N > 0:
        
