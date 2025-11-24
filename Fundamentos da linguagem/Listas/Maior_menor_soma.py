TAM = 5

lista = []
soma = 0

for i in range(TAM):
  num = int(input(f" Digite o {i+1}º número da lista: "))
  soma += num
  lista.append(num)

maior = lista[0]
menor = lista[0]

for i in range(TAM-1):
  if maior<lista[i+1]:
    maior=lista[i+1]
    
  if menor>lista[i+1]:
    menor = lista[i+1]

print(f" Soma do números da lista = {soma}")
print(f" Maior número da lista: {maior}")
print(f" Menor número da lista: {menor}\n")
