musica1 = input().lower()
musica2 = input().lower()
musica3 = input().lower()
musica4 = input().lower()
musica5 = input().lower()
pontuacao = 0

if musica1 == 'pelados em santos' or musica1 == 'vira-vira' or musica1 == 'robocop gay' or musica1 == '1406' or musica1 == 'mundo animal':
  pontuacao +=1
  
if musica2 == 'pelados em santos' or musica2 == 'vira-vira' or musica2 == 'robocop gay' or musica2 == '1406' or musica2 == 'mundo animal':
  pontuacao +=1

if musica3 == 'pelados em santos' or musica3 == 'vira-vira' or musica3 == 'robocop gay' or musica3 == '1406' or musica3 == 'mundo animal':
  pontuacao +=1

if musica4 == 'pelados em santos' or musica4 == 'vira-vira' or musica4 == 'robocop gay' or musica4 == '1406' or musica4 == 'mundo animal':
  pontuacao +=1

if musica5 == 'pelados em santos' or musica5 == 'vira-vira' or musica5 == 'robocop gay' or musica5 == '1406' or musica5 == 'mundo animal':
  pontuacao +=1

if 1 >= pontuacao >= 0:
  print("Errou feio, errou rude: 0 pontos")  
elif 3 >= pontuacao >= 2:
  print("Ate que tu foi bem mas nao chegou la: 1 ponto")
elif pontuacao == 4:
  print("Quase perfeito mano: 3 pontos")
elif pontuacao == 5:
  print("Parabens voce e um genio conhecedor da musica brasileira, voce merece 5 pontos")