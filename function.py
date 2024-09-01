"""
Defina uma função chamada hello, que recebe dois parâmetros: nome e idade. A função executa as seguintes ações:

Imprime uma mensagem de saudação: A função imprime "Olá" seguido do nome fornecido.
Verifica a idade: A função verifica se a idade (convertida para um número inteiro) é maior que 17.
Se a idade for maior que 17, a função imprime "Você deve se alistar!".
Se a idade for 17 ou menor, a função imprime "Você ainda não pode se alistar!".
"""

def hello(nome, idade):
    print(f"Olá {nome} !")
    if int(idade) > 17:
        print("Você deve se alistar !")
    else:
        print("Você ainda não pode se alistar !")

"""
A função hello recebe um nome e uma idade, cumprimenta a pessoa pelo nome e verifica se ela já tem idade suficiente para se alistar. 
A verificação é feita comparando se a idade é maior que 17.
"""        

hello("João", 18)
hello("Luan", 15)
hello("Lucas", "20")
hello(idade = 14, nome = "Cicero") # Aqui os argumentos são passados como nomeados, com nome sendo "Cicero" e idade sendo 14, e na ordem invertida dos parâmetros da função.
