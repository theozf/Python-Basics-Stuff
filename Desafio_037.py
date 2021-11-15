'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
VER DEPOIS A AULA DO GUANABARA SOBRE'''

n = int(input('Insira um número: '))
conv = int(input('Informe qual a base de conversão deseja (1 - binário; 2 - octal; 3 - hexadecimal): '))
if conv == 1:
    print(n**2)
elif conv == 2:
    print(n**8)
elif conv == 3:
    print(n)