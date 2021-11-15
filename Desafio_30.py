'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR'''
print('-'*27)
print('VERIFICADOR DE PAR OU ÍMPAR')
print('-'*27)
n = int(input('Digite um número: '))
if n % 2 == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÍMPAR'.format(n))
