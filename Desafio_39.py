'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele
ainda
vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
ano = int(input('Insira o ano de nascimento: '))
idade = 2021 - ano
alist = abs(idade-18)
anoAlist = ano + 18
if idade > 18:
    print(f'Você devia ter se alistado há {alist} anos, em {anoAlist}!\nAliste-se o quanto antes para evitar a perda de direitos'
          f'cívicos e políticos.')
elif idade == 18:
    print('Você está na idade exata para se alistar!')
else:
    print(f'Ainda faltam {alist} anos para você se alistar.\nVocê deve se alistar em {anoAlist}.')

