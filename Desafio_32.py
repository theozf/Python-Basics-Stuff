'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
from datetime import datetime
ano = int(input('Insira um ano ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é ano bissexto'.format(ano))
else:
    print('{} não é ano bissexto'.format(ano))

