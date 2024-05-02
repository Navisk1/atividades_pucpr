# toda vez que o peso excede 50 quilos, se deve pagar uma multa de R$4.00
#ler a variável peso
#calcular o excedente
#gravar na variável excesso o valor além do limite
#na variável multa, o valor que joão deve pagar

print('vamos calcular os quilos do peixe!')
fish = float(input("coloque aqui os quilos do peixe:"))
print(f"voce pescou {fish} quilos")
if fish > 50:
    excesso = fish - 50
    multa = excesso *4
    print(f"voce passou {excesso} quilos do permitido")
    print(f"por isso vai pagar: {multa} Reais de multa")

else:
    print("voce não excedeu o peso!")


