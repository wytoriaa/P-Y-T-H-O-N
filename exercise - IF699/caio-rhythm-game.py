mov1 = input()
mov2 = input()
mov3 = input()
mov4 = input()
mov5 = input()
#qtd de movimentos
movimentos = 0

#comeca com zero e vai incrementando a medida q ele vai se movimentando
if mov1 == 'direita' or mov1 == 'esquerda' or mov1 == 'cima' or mov1 == 'baixo':
  movimentos +=1 
if mov2 == 'direita' or mov2 == 'esquerda' or mov2 == 'cima' or mov2 == 'baixo':
  movimentos +=1 
if mov3 == 'direita' or mov3 == 'esquerda' or mov3 == 'cima' or mov3 == 'baixo':
  movimentos +=1 
if mov4 == 'direita' or mov4 == 'esquerda' or mov4 == 'cima' or mov4 == 'baixo':
  movimentos +=1 
else:
  movimentos +=1
#condicoes para o resultado de acordo com a quantidade de movimentos
if movimentos == 0:
  print('O jogador nao fez nenhuma entrada valida')
#O jogador não pode usar nenhum comando que não seja as quatro setas direcionais (cima, baixo, esquerda, direita
elif movimentos != mov1 or movimentos != mov2 or movimentos != mov3 or mov4!=movimentos:
  print(f'O jogador fez {movimentos} movimento(s) e tentou uma entrada invalida')
elif 4 < movimentos >= 5:
  print('O jogador conseguiu fazer todos 5 movimentos com sucesso!')