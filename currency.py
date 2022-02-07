availableCurrency = ['BTC', 'EUR', 'USD', 'PLN', 'TRY', 'YEN']
currencyValues = {
    'BTC': 0.000024,
    'EUR': 0.88,
    'USD': 1,
    'PLN': 3.96,
    'TRY': 13.45,
    'YEN': 114.58
}

def calcCurrency():
    print(f"Dostepne waluty: {', '.join(availableCurrency)}")
    # Waluta 1
    cur1 = input('\nPodaj pierwsza walute: ').upper()
    num1 = float(input('Podaj wartosc pierwszej waluty: '))
    # Waluta 2
    cur2 = input('Podaj druga walute: ').upper()

    if cur1 in currencyValues and cur2 in currencyValues: 
        print(f'{num1} {cur1} = {(num1 / currencyValues[cur1]) * currencyValues[cur2]} {cur2}')
    else:
        print('Bledne Dane')