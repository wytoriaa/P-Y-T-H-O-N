import math 
#ele tem que ter uma pontuação para passar para a próxima fase, 
#ele começa com 0 pontos
pontos = 0
#frases dos jurados
frase1 = input()
frase2 = input()
frase3 = input()
frase4 = input()

if frase1 == 'Sua apresentacao foi incrivel!':
    pontos +=200
if frase1 == 'Voce errou algumas notas, mas tem potencial':
    pontos = math.sqrt(pontos) +pontos
if frase1 == 'Sua performance me deu dor de cabeca!':
    if pontos > 100:
      pontos -= 100
    else:
      pontos = 0
      
if frase2 == 'Sua apresentacao foi incrivel!':
    pontos +=200
if frase2 == 'Voce errou algumas notas, mas tem potencial':
    pontos = math.sqrt(pontos) +pontos
if frase2 == 'Sua performance me deu dor de cabeca!':
    if pontos > 100:
      pontos -= 100
    else:
      pontos = 0
      
if frase3 == 'Sua apresentacao foi incrivel!':
    pontos +=200
if frase3 == 'Voce errou algumas notas, mas tem potencial':
    pontos = math.sqrt(pontos) +pontos
if frase3 == 'Sua performance me deu dor de cabeca!':
    if pontos > 100:
      pontos -= 100
    else:
      pontos = 0
      
if frase4 == 'Sua apresentacao foi incrivel!':
    pontos +=200
if frase4 == 'Voce errou algumas notas, mas tem potencial':
    pontos = math.sqrt(pontos) +pontos
if frase4 == 'Sua performance me deu dor de cabeca!':
    if pontos > 100:
      pontos -= 100
    else:
      pontos = 0

if pontos > 150:
  print(f'Parabens! Voce atingiu a pontuacao de {pontos:.2f} e passou para a proxima fase!')
elif 100 <= pontos <= 150:
  print('Foi por pouco! Voce tem que ajustar algumas notas para alcancar a pontuacao necessaria')
else:
  print("A area musical nao foi feita para voce!")
