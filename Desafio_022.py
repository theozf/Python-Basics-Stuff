'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''
#linha 11 o  - nome.count(' ') é a forma para a máquina contar os espaços e eliminará, por causa do -
nome = str(input('Qual é o seu nome completo? ')).strip()
separa = nome.split()
print('Analisando seu nome...')
print('Seu nome é', nome)
print('Em maiúsculo fica {}'.format(nome.upper()))
print('Em minúsculo fica {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa [0])))











