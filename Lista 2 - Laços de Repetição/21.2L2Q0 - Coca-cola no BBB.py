#Voce recebera a quantidade que participantes da prova:
competitor_n = int(input())

#A pessoa que encontrar mais latinhas ganha a prova
cans_s = 0 #o jogador comeca com zero latinhas
winner = ""
count = 1 #começamos a contar a partir daqui

while count != competitor_n:
  #Em seguida, receberá o nome de um competidor 
  #e depois quantidade de latinhas arrecadadas por ele, N vezes
  player = input()
  cans = int(input())
  if cans > cans_s:
    cans_s = cans 
    winner = player
  count+=1
  
print(f'{winner} e o novo anjo!')