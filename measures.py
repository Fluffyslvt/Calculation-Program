availableMeasurements = ['cm', 'cal', 'stopy', 'm', 'km', 'mile']
measuresValues = {
    'cm': 100,
    'cal': 39.37,
    'stopy': 3.28,
    'm': 1,
    'km': 0.001,
    'mile': 0.000621371192
}

def calcMeasurement():
    print(f"Dostepne miary: {', '.join(availableMeasurements)}")
    # Miara 1
    mes1 = input('\nPodaj pierwsza miare: ')
    num1 = float(input('Podaj wartosc pierwszej miary: '))
    # Miara 2
    mes2 = input('Podaj druga miare: ')

    if mes1 in measuresValues and mes2 in measuresValues: 
        print(f'{num1} {mes1} = {(num1 / measuresValues[mes1]) * measuresValues[mes2]} {mes2}')
    else:
        print('Bledne Dane')