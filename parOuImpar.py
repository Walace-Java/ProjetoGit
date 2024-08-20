import random

pAndI = str(input('Você escolher (P) par ou (I) impar? '))
print('sorteando numero...')
numero = random.randint(1, 100)

if numero % 2 == 0:
    print('o numero sorteado foi {} portando ele é par'.format(numero))
    if pAndI == 'p':
        print('Você ganhou')
    elif pAndI == 'i':
        print('sinto muito você perdeu')

elif numero % 2 == 1:
    print('o numero sorteado foi {} portanto ele é impar'.format(numero))
    if pAndI == 'i':
        print('parabens você ganhou!')
    elif pAndI == 'p':
        print('Voce perdeu!')
