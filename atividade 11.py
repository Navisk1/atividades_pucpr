print("quanto vou ganhar no final do mês?")
TIME = float(input("escreva aqui as horas que você trabalha no mes:"))
MONEY = float(input("agora, coloque aqui o quanto voce ganha por hora:"))
soma = (TIME*MONEY)
print('esse é o valor bruto que voce ganha por mes',soma)
#INSS
des1 = soma -(soma*0.8)/100
print("valor com o desconto no INSS:R$",des1)
#sindicato
sind = soma - (soma*0.5)/100
print("o valor com o desconto do sindicato:R$",sind)
#salário liquido
sal = soma - (soma*8.0)/100 - (soma*0.5)/100
print("o seu salário liquido:R$",sal)