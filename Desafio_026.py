'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
f = str(input('Escreva uma frase qualquer: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(f.count('A')))
print('A primeira letra A aparece na posição {}'.format(f.find('A')+1)) #+1 pra não ficar sendo 0 a primeira posição
print('A última letra A aparece na posição {}'.format(f.rfind('A')+1))



