'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''
from math import trunc
n = float(input('Digite um número Real: '))
print('A forma inteira de {} é {}'.format(n, trunc(n)))

'''ou então pode fazer assim:
n = float(input('Digite um número Real: '))
print('A forma inteira de {} é {}'.format(n, int(n)))'''




