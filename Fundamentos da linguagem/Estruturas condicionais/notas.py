NUM = 2

soma = 0
nome = input(" Informe o nome do aluno: ")
               
for i in range(NUM):
  nota = int(input(f" Informe a {i+1}º nota: "))
  soma += nota

if (soma/NUM)>= 7:
  print(f" Aluno(a) {nome} foi Aprovado(a)!")
else:
  print(f" Aluno(a) {nome} Reprovado(a)!")


