genero = str(input())
nacional = str(input())
decada = str(input())

if genero == 'Rock':
  if nacional == 'Nao' and decada == '70':
    print('A musica que voce esta procurando eh: Bohemian Rapsody')
  elif nacional == 'Sim' and decada == '70':
    print('A musica que voce esta procurando eh: O Pirata')
  elif nacional == 'Sim' and decada == '80':
    print('A musica que voce esta procurando eh: Indios')
  else:
    print('Musica nao encontrada')

elif genero == 'Samba':
  if nacional == 'Sim' and decada == '80':
    print('A musica que voce esta procurando eh: Conselho')
  elif nacional == 'Sim' and decada == '70':
    print('A musica que voce esta procurando eh: Apesar de Voce')
  elif nacional == 'Sim' and decada == '60':
    print('A musica que voce esta procurando eh: Mas que Nada')
  else:
    print('Musica nao encontrada')

elif genero == 'Pop':
  if nacional == 'Nao' and decada ==  '90':
    print('A musica que voce esta procurando eh: Candle in the Wind 1997')
  elif nacional == 'Nao' and decada == '80':
    print('A musica que voce esta procurando eh: Take On Me')
  elif nacional == 'Sim' and decada == '90':
    print('A musica que voce esta procurando eh: Anna Julia')
  else:
    print('Musica nao encontrada')
else:
    print('Musica nao encontrada')