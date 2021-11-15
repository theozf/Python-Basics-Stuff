'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira mais um número: '))
menor = n1
if n1>n2 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor número é {} e o maior número é {}'.format(menor, maior))



