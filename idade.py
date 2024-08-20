idade = int(input('digite sua idade!'))

if idade <= 12:
    print('você ainda é uma criança!');

elif idade >= 13 and idade <= 17:
    print('você já é um adolescente')

elif idade >=18 and idade <=64:
    print('você é um adulto')
else:
    print('ou você é um idoso, ou esta morto')
