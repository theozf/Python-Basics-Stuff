'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
print('-'*41)   #usei len() pra contar qntas strings tem pros traços cobrirem a frase
print('RADAR DE VELOCIDADE DA POLÍCIA RODOVIÁRIA')
print('-'*41)
vel = float(input('Velocidade detectada: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('VOCÊ EXCEDEU O LIMITE DE 80KM/H E DEVE PAGAR UMA MULTA NO VALOR DE R$ {:.2f}'.format(multa))
else:
    print('VOCÊ ESTÁ DENTRO DO LIMITE PERMITIDOD DE VELOCIDADE')
print('Tenha um bom dia! Dirija com segurança!')







