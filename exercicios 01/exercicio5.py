#Receba do usuário três informações: um número inteiro, um número decimal e uma palavra.

#Receba o número inteiro
number1 = int(input("Digite um número inteiro: "))

#Receba o número decimal
number2 = float(input("Digite um número decimal: "))

#Receba uma palavra
palavra = input("Digite uma palavra: ")

#Mostra as informações digitadas e seus tipos.
#print(f"Foi digitado: {number1} = {type(number1)}, {number2:.2f} = {type(number2)}, {palavra} = {type(palavra)}")

print(f"Foi digitado o inteiro {number1}, o decimal {number2} e a palavra {palavra}")
