n = int(input()) #chefes

#Obrigatoriamente, nenhum chefe pode receber uma média menor ou igual a 0.
media_max = 10
vencedor = ""
count = 1

while (count != n):
  nome = input()
  nota1 = float(input())
  nota2 = float(input())
  nota3 = float(input())
  
  media = (nota1 + nota2 + nota3)/3
  
  if media <= media_max:
    media_max = media
    vencedor = nome
  
  count += 1
if media_max > 0:
  print(f'O chef eliminado da vez é: {vencedor} - {media_max:.2f}')
else:
  print("Ocorreu um erro no sistema de notas, por favor insira notas validas")