destino = int(input()) #destino
comeco = 0 #ponto de partida

#Em seguida, o programa receberá um número indefinido de inteiros 
# positivos que correspondem ao progresso do casal, 
# sempre terminando com um número negativo, 
# o número negativo não deve ser considerado no calculo do progresso:

atual = 0 #pegar a entrada dentro do loop

while atual >= 0:
  atual = int(input())
  if atual > 0:
    for caminhos in range(0, atual + 1):
      comeco += caminhos

if comeco < destino:
  print("Ainda nos falta um pouco...")
elif comeco == destino:
  print("Pode beijar a noiva, afinal, vocês conseguiram!")
elif comeco < destino * 20:
  print("Parece que os pombinhos passaram um pouco do local...")
elif comeco <= destino * 100:
  print("Acho que nos perdemos um pouco no caminho, onde estamos?")
else:
  print("Hum... acho que o casal deve rever seus votos de matrimônio...")