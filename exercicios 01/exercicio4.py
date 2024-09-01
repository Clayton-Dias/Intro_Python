#Fazer uma calculadora com as operações básicas: '+' (adição), '-' (subtração) , '*' (multiplicação) e '/'(divisão)

print("Para realizar o cálculo desejado, siga a orientações abaixo.")
print("Aviso: use '.' no lugar da ',' .")

#Recebe o 1º número 
num1 = float(input("Digite o primeiro número: "))

#Recebe a operação desejada
op = input("Digite a operação desejada para ser realizada ( + , - , * ou / ): ")

#Recebe o 2º número
num2 = float(input("Digite o segundo número: "))


#Mostra o valor da operação de acordo com o operador indicado pelo usuário
if op == "+":
    print(f"{num1:.2f} + {num2:.2f} = {(num1+num2):.2f}") # Adição
elif op == "-":
     print(f"{num1:.2f} - {num2:.2f} = {(num1-num2):.2f}") # Subtração
elif op == "*":
    print(f"{num1:.2f} * {num2:.2f} = {(num1*num2):.2f}") # Multiplicação
elif op == "/":
    if num2 == 0: #Verifica se o divisor(num2) é 0
        print(f"Operação Invalida, pois não há divisão por 0.") 
    else:
        print(f"{num1:.2f} / {num2:.2f} = {(num1/num2):.2f}") # Divisão
else:
    print(f"Operação Invalida, pois o operador {op} informado não é válido.")
