'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random
print('BEM VINDO AO JOGO DE ADIVINHA')
print('-'*29)
print('Eu estou pensando em um número entre 1 e 5')
#n = [1, 2, 3, 4, 5]
#escolha = random.choice(n)
computador = random.randint(1, 5)
num = int(input('Em que número estou pensando? '))
if num == computador:
    print('PARABÉNS! VOCÊ ACERTOU!!!')
else:
    print('INFELIZMENTE VOCÊ ERROU, EU PENSEI NO NÚMERO {}'.format(computador))


