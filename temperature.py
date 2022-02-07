# przelicznik temperatur (Kelvin, Farenheit, Celsius, Ramkina)
availableTemperature = ['Farenheit', 'Kelvin', 'Rankina']

def calcTemperature():
    print(f"Dostepne temperatury: {', '.join(availableTemperature)}")
    temp1 = float(input('Podaj temperature(°C): '))
    temp2 = input('Podaj druga temperature: ').lower().capitalize()

    if temp2 == 'Farenheit': 
        print(f'{temp1}°C = {(temp1 * 1.8) + 32}°F')
    elif temp2 == 'Kelvin':
        print(f'{temp1}°C = {temp1 + 273.15}K')
    elif temp2 == 'Rankina':
        print(f'{temp1}°C = {(temp1 + 273.15) * 1.8}°R')
    else:
        print('Bledne Dane')
        