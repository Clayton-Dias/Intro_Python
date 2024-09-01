#Crie um programa que peça ao usuário três números (pode ser decimal ou inteiro) e calcule a média desses números. 
#O programa deve exibir a média com duas casas decimais.

#
print("Digite 3 números para que seja realizada a média.")

#Receba o primeiro número
num1 = float(input("Digite 1º número: "))

#Receba o segundo número
num2 = float(input("Digite 2º número: "))

#Receba o terceiro número
num3 = float(input("Digite 3º número: "))

#Cálculo da média do números digitados
#media = (num1 + num2 + num3) / 3

#Mostra a média dos números digitados.
#print(f"A média dos números digitados é {media}")
print(f"A média dos números digitados é {((num1+num2+num3)/3):.2f}")