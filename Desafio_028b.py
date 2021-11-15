from random import randint
from time import sleep
print('BEM-VINDO (A) AO JOGO DE ADIVINHAÇÃO')
print('--'*25)
print('Pensei em um número de 1 a 5, tente adivinhar aí.')
print('--'*25)
computador = randint(1, 5)
jogador = int(input('Em qual número será que eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('VOCÊ GANHOU!')
else:
    print('EU GANHEI! Eu pensei no número {}'.format(computador))


