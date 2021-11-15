'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''
sal = float(input('Digite seu salário: '))
if sal <= 1250:
    print('Você recebeu 15% de aumento, parabéns! AGORA SEU SALÁRIO É R${:.2f}'.format(sal + (sal * 15 / 100)))
else:
    print('Você recebeu 10% de aumento, parabéns! AGORA SEU SALÁRIO É R${:.2f}'.format(sal + (sal * 10 / 100)))


