'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''
d = float(input('Qual a distância da sua viagem (em Km)? '))
if d <= 200:
    print('O preço da passagem é R${:.2f}'.format(d * 0.5))
else:
    print('O preço da passagem é R${:.2f}'.format(d * 0.45))
print('DESEJAMOS A VOCÊ UMA BOA VIAGEM!')
