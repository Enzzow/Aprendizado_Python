def dobro (list):
    list2 = []

    for i in range(len(list)):
        list2.append(list[i]*2)
    
    return list2


tam = int(input("\n Informe o tamanho da lista: "))
print("\n")

lista = []

for i in range (tam):
    num = int(input(f" Informe o {i+1}º número da lista: "))
    lista.append(num)

print(f" \nLista original: {lista}\n")

print(f" Lista com valores dobrados: {dobro(lista)}\n ")
