#Receba uma temperatura em Celsius do usuário
temp = float(input("Digite a temperatura em Celsius(°C): "))

#Fórmula para conversão é Fahrenheit: F = C * 9/5 + 32

#Conversão
#F = temp * 9/5 + 32

#Mostra a temperatura convertida para Fahrenheit
print(f"A temperatura informada em Fahrenheit é {(temp * 9/5 + 32):.2f} °F")

#print(f"A temperatura informada em Fahrenheit é {F :.2f}")

# ':.xf' limita o número de casa decimal que será mostrado   
