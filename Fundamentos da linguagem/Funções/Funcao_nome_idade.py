def formatado (nome,idade):
    print(" \n&|Status|&\n")
    print(f" Nome: {nome}")
    print(f" Idade: {idade}\n")

nome = input("\n Informe o seu nome: ")
idade = int(input(" Informe a sua idade: "))

formatado(nome,idade)