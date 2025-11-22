def num_positivos(list):
    list2 = []

    for i in range(len(list)):
        if (list[i] >= 0):
           list2.append(list[i])

    return list2

lista = [1,2,3,-4,5]
print(f" Lista original: {lista}")

lista2 = num_positivos(lista)

print(f" Lista modificada: {lista2}")