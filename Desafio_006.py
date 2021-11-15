print('Vamos calcular o dobro, triplo e raiz quadrada de um número?')
n = int(input('Informe um número: '))
print('O dobro de {} é {}'.format(n, (n*2)))
print('O triplo de {} é {}\nA raíz quadrada de {} é {:.2f}'.format(n, (n*3), n, pow(n, (1/2))))

#ou: (porém assim ocupa mais memória, por ter mais variáveis
#n = int(input('Informe um número: '))
#d = n*2
#t = n*3
#rq = n**1/2   #ou usar: pow(n, (1/2)) - pow é para potência, coloca-se a base vírgula o valor a elevar
#print('O dobro de {} é {}, o triplo é {} e sua raíz quadrada é {}'.format(n, d, t, rq))

