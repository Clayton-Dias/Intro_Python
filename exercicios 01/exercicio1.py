"""
print("Digite sua idade:")
age = int(input())

if age>= 16:
    print("Você está elegível para votar")
else:
    print("Você está inelegível para votar")
"""

#Receber a idade do usuário como inteiro em uma variavél.
print("Para verficar se você está apto ou inapto para votar.")
idade = int(input("Digite sua idade: "))

#Valida a idade para verificar se está apto ou inapto para votar.
#Informar ao usuário se está apto ou inapto para votar.
#Idade minima é 16 anos.
if idade >= 16:
    print("Você está apto para votar")
else:
    print("Você está inapto para votar")
