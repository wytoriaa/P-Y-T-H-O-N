n = input() #Letra sorteada
x = int(input()) #Quantidade de participantes

letter_count = 0 #essa variavel vai contar as vezes em que a letra apareceu

#Nome do participante e palavra escolhida
winner = ""  #o nome do vencendor
winner_word = ""  #palavra vencedora
for competidor in range(x): 
  #for para passar pelo range de x, ja que existe a qtd de letras
  count = 0 #contador 
  name, word = input().split("-")
  name = str(name)
  word = str(word)
  for letter in word: #o letter para a letra e word para saber a palavra
    if letter == n: #se a letra for a letra sorteada
      count += 1 #incrementa 1 no contador
    if letter_count < count: #se a qtd de vezes da letra for menor q o contador
      letter_count = count #a quantidade de letra sera a mesma do contador
      winner = name #o vencedor vai ser o nome
      winner_word = word #a palavra vencedora vai ser a palavra sorteada
if winner == "Prior":
    print(f"Joga y joga! Mago Prior e o novo lider com a palavra {winner_word} com {letter_count} aparicoes da letra {n}.")
else:
    print(f"Vish! O Mago Prior pode ir pro paredao, ja que quem ganhou foi {winner}, com a palavra {winner_word} e {letter_count} aparicoes da letra {n}.")