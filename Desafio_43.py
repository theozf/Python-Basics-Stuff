peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / (altura**2)
print(f'SEU IMC É: {imc:.2f}')
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25:
    print('VOCÊ ESTÁ NO PESO IDEAL')
elif imc > 25 and imc <=30:
    print('VOCÊ ESTÁ SOBREPESO')
elif imc > 30 and imc <= 40:
    print('VOCÊ ESTÁ OBESO')
else:
    print('VOCÊ ESTÁ OBESO MÓRBIDO')
