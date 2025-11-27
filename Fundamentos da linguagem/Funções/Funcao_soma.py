def retorna_soma (lista):
    
    soma = 0

    for numero in lista:
        soma+=lista[i]
    
    return soma

tam = int(input("\n Informe o tamanho da lista: "))
lista = []
print("\n")

for i in range(tam):
    num = int(input(f" Digite o {i+1}º número da lista: "))
    lista.append(num)

print(f"\n Resultado da soma: {retorna_soma(lista)}\n")