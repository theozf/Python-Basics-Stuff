'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo. Calcule e mostre o comprimento da hipotenusa.'''
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hip))


