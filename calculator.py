def calc():
    num1 = float(input('\nPodaj pierwsza liczbe: '))
    num2 = float(input('Podaj druga liczbe: '))
    calcOption = input('Wybierz rodzaj dzialania: +  -  *  / ')
    print('')

    if calcOption == '+':
        print(f'{num1} + {num2} = {num1 + num2}')

    elif calcOption == '-':
        print(f'{num1} - {num2} = {num1 - num2}')

    elif calcOption == '*':
        print(f'{num1} * {num2} = {num1 * num2}')

    elif calcOption == '/':
        if num2 != 0: # sprawdzanie czy num2 nie jest zerem
            print(f'{num1} / {num2} = {num1 / num2}')
        else:
            print('BLAD - dzielenie przez zero')