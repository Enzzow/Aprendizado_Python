string = input("Digite uma string: ").lower()

vogais = ['a','e','i','o','u']
qntd = 0

for i in range(len(string)):
    for ii in range(len(vogais)):
        if string[i]==vogais[ii]:
            qntd+=1

print(f" Nº de vogais: {qntd}")

