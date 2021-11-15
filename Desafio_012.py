#Faça um algoritmo que leia o preço de um produto e mostre
#seu novo preço, com 5% de desconto
p = float(input('Digite o preço do produto: '))
d = (p*5)/100
pf = p-d
print(f'O preço do produto com 5% de desconto é R${pf:.2f}')



