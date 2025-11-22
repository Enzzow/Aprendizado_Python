string = input(" Informe uma string e descubra se é um palíndromo: ")

string_invertida = string[::-1] #String invertida

if (string == string_invertida):
    print(" É um palíndromo")
else:
    print(" Não é um palíndromo")
    