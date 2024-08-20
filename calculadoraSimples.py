tipo = int(input('qual calculo deseja realizar?? \n'
                    '1. +\n'
                    '2. -\n'
                    '3. x\n'
                    '4. /\n'))
if tipo == 1:
    calculo = int(input('digite o valor um que deseja somar\n'))
    calculo2 = int(input('{} + '.format(calculo)))
    resultado = calculo + calculo2
    print('{} + {} = {} '.format(calculo, calculo2, resultado))

elif tipo == 2:
    calculo = int(input('digite o valor para a subtração\n'))
    calculo2 = int(input('{} - '.format(calculo)))
    resultado = calculo - calculo2
    print('{} - {} = {}'.format(calculo, calculo2, resultado))

elif tipo == 3:
    calculo = int(input('digite o valor para a multiplicação\n'))
    calculo2 = int(input('{} x '.format(calculo)))
    resultado = calculo * calculo2
    print('{} x {} = {}'.format(calculo, calculo2, resultado))

elif tipo == 4:
        calculo = int(input('digite o valor para a divisão\n'))
        calculo2 = int(input('{} / '.format(calculo)))
        resultado = calculo / calculo2
        print('{} x {} = {}'.format(calculo, calculo2, int(resultado)))
else:
    print('por favor, escolher uma das alternativas acima digitando o numero correspondente ao calculo')
