idade = int(input(" Informe a sua idade: ")
while idade<0:
 print(" Inválido!\n")
 idade = int(input(" Informe a sua idade: "))

print(" Faixa etária: ",end="")             
if idade<=11:
  print(" Criança")
elif idade<=18:
  print(" Adolescente")
elif idade<=64:
  print(" Adulto")
else:
  print(" Idoso")
