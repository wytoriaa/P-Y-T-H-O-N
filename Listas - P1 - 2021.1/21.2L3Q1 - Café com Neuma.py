n = int(input())
mulherzinhas = []
hominhos = []

for i in range(n):
  nome, genero = input().split(" - ")
  if genero == "F":
    mulherzinhas.append(nome)
  else:
    hominhos.append(nome)
    
hominhos_nome = ""  
mulherzinhas_nome = ""

#Caso só tenham meninos na lista
if len(hominhos) > 0 and len(mulherzinhas) == 0:
  for nome in hominhos:
    hominhos_nome += nome + ", "
  print(f"{hominhos_nome}Querem cafe?")
  print(f"Serao necessarias {len(hominhos)} porcoes de cafe")

#Caso tenham meninos e meninas na lista 
elif len(mulherzinhas) > 0 and len(hominhos) > 0:
  for nome in hominhos:
    hominhos_nome += nome + ", "
  print(f"{hominhos_nome}Querem cafe?")
  
  for nome in mulherzinhas:
    mulherzinhas_nome += nome + ", "
  print(f"{mulherzinhas_nome}Desculpa, so pros meninos HAHAHAHAAHHAHAHA")
  print(f"Serao necessarias {len(hominhos)} porcoes de cafe")
  
#Caso só tenham meninas na lista
else:
  for nome in mulherzinhas:
    mulherzinhas_nome += nome + ", "
  print(f"{mulherzinhas_nome}Desculpa, so pros meninos HAHAHAHAAHHAHAHA")
  print(f"Nao tem meninos na lista, nao precisa fazer cafe, Neuma")