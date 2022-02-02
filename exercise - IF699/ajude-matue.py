obj1 = input()
obj2 = input()
obj3 = input()
obj4 = input()

ferramenta = 0

if obj1 == 'Alicate' or obj1 == 'Chave de Fenda' or obj1 == 'Lanterna' or obj1 == 'Martelo':
  ferramenta +=1
if obj2 == 'Alicate' or obj2 == 'Chave de Fenda' or obj2 == 'Lanterna' or obj2 == 'Martelo':
  ferramenta +=1
if obj3 == 'Alicate' or obj3 == 'Chave de Fenda' or obj3 == 'Lanterna' or obj3 == 'Martelo':
  ferramenta +=1
if obj4 == 'Alicate' or obj4 == 'Chave de Fenda' or obj4 == 'Lanterna' or obj4 == 'Martelo':
  ferramenta +=1

if ferramenta == 4:
  print('Tuê, encontrei tudo! Tá tudo Jóia, ficou bem BOOMZIM!!!')
elif ferramenta == 0:
  print('Tuêzin! Se a seca chegar, não vai se desanimar...')
else:
  print('Andam dizendo que o Tuê é um baiano...')