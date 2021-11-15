'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input('Informe o valor da casa: '))
sal = float(input('Informe seu salário (mensal): '))
ano = int(input('Em quantos anos você pretende pagar a casa: '))
prestacao = casa / (ano*12)
print(f'A casa pretendida custa R${casa:.2f} e você gostaria de {ano} ano(s) de financeiamento.', end='')
print(f' A prestação será de R${prestacao:.2f}.')
if prestacao > (sal*30/100):
    print('INFELIZMENTE SEU PEDIDO DE EMPRÉSTIMO FOI NEGADO, POIS A PRESTAÇÃO EXCEDE 30% DE SEU SALÁRIO.')
else:
    print('SUA SOLICITAÇÃO DE EMPRÉSTIMO FOI APROVADA!')