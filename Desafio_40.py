'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
m = (n1+n2) / 2
if m >= 7:
    print('VOCÊ FOI APROVADO!')
elif m < 7 and m >= 5:
    print('VOCÊ ESTÁ EM RECUPERAÇÃO')
else:
    print('VOCÊ FOI REPROVADO! :(')
