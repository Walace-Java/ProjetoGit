comprar = int(input('o que deseja comprar, temos os seguintes itens \n'
                    '1 cerveja\n'
                    '2 cereal\n'
                    '3 amendoim\n'))
if comprar == 1:
    idade = int(input('quantos anos voce tem '))
    if idade <18:
        print('sinto muito, mas você não pode comprar isso')
    else:
        print('custa 8 reais')

elif comprar == 2:
    print('muito bem, custa 2 reais')

elif comprar == 3:
    print('pode comprar, custa 7 reais')
else:
    print('por favor, selecione uma das opções')
