'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''
cid = str(input('Digite o nome de uma cidade: ')).strip()
print(cid[0:5].upper() == 'SANTO')

#por tudo em maísculo para evitar erro caso usuário coloque letras minusculas e maiusculas
#a variável recebe o valor ('nome da cidade'), joga todos os caraceteres em maiusculo, daí sim verifica se há santo no nome



