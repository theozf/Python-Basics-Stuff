ano = int(input('Informe o ano de nascimento do atleta: '))
idade = 2021 - ano
if idade <= 9:
    print(f'O ATLETA TEM {idade} ANOS.\nCATEGORIA: MIRIM')
elif idade <= 14 and idade > 9:
    print(f'O ATLETA TEM {idade} ANOS.\nCATEGORIA: INFANTIL')
elif idade <= 19 and idade > 14:
    print(f'O ATLETA TEM {idade} ANOS.\nCATEGORIA: JÚNIOR')
elif idade > 19 and idade <= 20:
    print(f'O ATLETA TEM {idade} ANOS.\nCATEGORIA: SÊNIOR')
else:
    print(f'O ATLETA TEM {idade} ANOS.\nCATEGORIA: MASTER')

