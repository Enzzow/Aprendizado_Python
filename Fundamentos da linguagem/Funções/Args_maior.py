def maior_valor(*numeros):
    maior = numeros[0]

    for i in range(len(numeros)-1):
        if maior<numeros[i+1]:
            maior = numeros[i+1]
    
    return maior


print(f" \n O maior número é {maior_valor(1,4,2,7,9)} \n")
        
