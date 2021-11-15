'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente.'''
nome = str(input('Qual é seu nome completo? ')).upper().strip().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0].capitalize()))
print('Seu último nome é {}'.format(nome[len(nome)-1].capitalize()))

#O -1 faz com que o programa detecte o último nome, pois uma lista começa com 0 até X (X ultimo nome),
#len conta de 1 pra frente, assim ele conta o 0 como primeiro elemento



