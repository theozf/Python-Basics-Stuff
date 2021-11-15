'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
não formar um triângulo.'''
a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B do triângulo: '))
c = float(input('Digite o lado C do triângulo: '))
if a < b+c and b < a+c and c < a+b:
    print('Os segmentos formam um triângulo! ', end='')
    if a == b == c:
        print('Este triângulo é EQUILÁTERO!')
    elif a != b != c != a:
        print('Este triângulo é ESCALENO!')
    else:
        print('Este triângulo é ISÓSCELES')
else:
    print('Não forma triângulo!')