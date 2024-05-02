# faça um programa que peça as horas trabalhadas e depois calcule o saário
print("quanto vou ganhar no final do mês?")
TIME = float(input("escreva aqui as horas que você trabalha no mes:"))
MONEY = float(input("agora, coloque aqui o quanto voce ganha por hora:"))
soma = (TIME*MONEY)
if soma <=1000:
    print('voce faltou muito, então vai receber esse valor',soma)

else:
    print("Bom trabalho, voce vai receber esse valor:",soma)