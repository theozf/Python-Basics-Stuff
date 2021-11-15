#Faça um algoritmo que leia o salário de um funcionário
#e mostre seu novo salário, com 15% de aumento
s = float(input('Informe seu salário: R$'))
a = (s*15)/100
sf = s+a
print(f'O seu novo salário, com 15% de aumento é R${sf:.2f}')
