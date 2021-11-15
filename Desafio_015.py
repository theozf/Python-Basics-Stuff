#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
#R$0,15 por Km rodado.
print('CALCULADORA DE PREÇO - CAPIVARAS: SERVIÇOS ALUGUEL DE CARROS E AGIOTAGEM DE MEIOS DE TRANSPORTE')
dia = int(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos kilometros foram rodados: '))
total = (dia * 60) + (km * 0.15)
print('O valor a ser pago é de R${:.2f}'.format(total))

