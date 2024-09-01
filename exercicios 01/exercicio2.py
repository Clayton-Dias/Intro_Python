"""
print("Digite um número inteiro:")
number = int(input())

x = number%2

if x == 0:
    print(f"O número {number} é par")
else:
    print(f"O número {number} é impar")
"""

#Receba um número inteiro do usuário.
numero = int(input("Digite um número inteiro: "))

#Verifcar se o número digitado é impar ou par e mostra ao usuário o resultado.
#O operador '%' indica o 'resto' da operação de uma divisão.
# Se igual a 0,o número é par, caso contrário, número é impar.
#Mostra a mensagem ao usuário, conforme a verificação.
if (numero % 2) == 0:
    print(f"O número {numero} é par") #Mensagem se é par
else:
    print(f"O número {numero} é impar") #Mensagem se é impar



