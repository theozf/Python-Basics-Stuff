print('CARTEIRA EM DÓLAR')
#Considere US$1.00 = R$5,62 (15/4/2021)
real = float(input('Quantos reais você tem na carteira? R$'))
dol = real/5.62
print(f'Com R${real}, você tem US${dol:.2f} na carteira.')



