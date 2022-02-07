import calculator, currency, temperature, measures

menuOption = ''
name = input('Witaj w programie! Podaj swoje imie: ')

while menuOption != '0':
    menuOption = input(f"""\n{name}, wybierz rodzaj zadania:
    1. Kalkulator,
    2. Przelicznik walut,
    3. Przelicznik temperatur,
    4. Przelicznik miar
    
    0. Wyjdz z programu
    """)

    print('')

    # Klasyczny Kalkulator
    if menuOption == '1':
        calculator.calc()

    # Przelicznik Walut
    elif menuOption == '2':
        currency.calcCurrency()

    # Przelicznik Temperatur
    elif menuOption == '3':
        temperature.calcTemperature()

    # Przelicznik miar
    elif menuOption == '4':
        measures.calcMeasurement()
