passos = [] #lista vazia, pq eu nao sei os passos
qtd_passos = 0 
passo = "" #vai os elementos que vao está dentro da lista passos

while passo != "FIM":
  passo = input()
  if passo != "FIM":
    passos.append(passo) #define o tamanho da lista
    qtd_passos += 1

print(f"Olá seguimores! O primeiro passo da dancinha é {passos[0]}")
print(f"Depois, a gente faz o {passos[1]} e {passos[2]}")
print(f"Temos ainda mais {qtd_passos - 3} passos pra aprender!")
print(f"Por último, vamos fazer o {passos[-1]}")