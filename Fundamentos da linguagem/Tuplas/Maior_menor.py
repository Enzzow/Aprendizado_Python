tupla = (1,2,3,0,30,5)
print(f"\n Tupla: {tupla}\n")

maior = tupla[0]
menor = tupla[0]

for i in range(len(tupla)-1):

    if tupla[i+1]>maior:
        maior = tupla[i+1]

    if tupla[i+1]<menor:
        menor = tupla[i+1]

print(f" Maior número da tupla: {maior}")
print(f" Menor número da tupla: {menor}\n")

