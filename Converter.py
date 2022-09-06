from glob import escape
from locale import currency


class TemperatureConverter():

    def fahrenheitToCelcius(self, temp):
        return (5/9) * (temp - 32)

    def celciusToFahrenheit(self, temp):
        return (9/5 * temp) + 32


class DistanceConverter():
    def milesToKm(self, miles):
        return miles * 1.60934

    def kmToMiles(self, km):
        return km * 0.621371
    
    def footToMeters(self, foot):
        return foot * 0.3048
    
    def metersToFoot(self, meters):
        return meters * 3.28084

    def yardToMeters(self, yard):
        return yard * 0.9144

    def metersToYards(self, meters):
        return meters * 1.09361
    
    def cmToInch(self, cm):
        return cm * 0.39370
    
    def inchtoCm(self, inch):
        return inch * 2.54


class CurrencyConverter():
    def nairaToDollar(naira):
        return naira * 600

    def dollarToNaira(dollar):
        return dollar * 0.0016666666666


class MassConverter():
    def kgToPound(self, kg):
        return kg * 2.20462
    
    def poundToKg(self, pound):
        return pound * 0.453592

    def gramToOunce(self, kg):
        return kg * 0.035274

    def OunceToGram(self, ounce):
        return ounce * 28.3495


Distance = {'submenu': ['Miles to Km', "Km to Miles", "Yard To meter", 'Meter to Yard', "Foot To Meter", "Meter to Foot", "Cm to Inch", "Inch To Cm"], "preamble": "Choose The Units "}
Currency= {'submenu': [{'Naira To Dollar': "Name"}, 'Dollar To Naira'], "preamble": "Choose The currency "}
Mass = {'submenu': ['Pound To Kg', "Kg to Pound", 'Gram To Ounce', "ounce To Gram"], "preamble": "Choose The Units "}
Temperature = {'submenu': ['Fahrenheit To celcius', "Celcius To Fahrenheit"], "preamble": "Choose The Units "}


MainMenu = {"submenu": ['Temperature', 'Distance', "Mass", "Currency"], 'preamble': "What do you wish to convert? ",  "submenus": [Temperature, Distance, Currency, Mass]}

def showMenu(menu):
    print(menu["preamble"])
    for index, item in enumerate(menu['submenu']):
        print("{index}. {item}".format(index = index+1, item = item))
    
    try:
        choice = int(input(" Please Choose From numbers provided: "))
        choice -= 1
        return menu['submenus'][choice]
    except:
        print("Invalid Entry.")


def submenu(menu):
    print(menu["preamble"])
    for index, item in enumerate(menu['submenu']):
        print("{index}. {item}".format(index = index+1, item = item))
    
    try:
        choice = int(input("\n Please Choose From numbers provided: "))
        choice -= 1
        print(menu["submenu"][choice])
    except:
        print("Invalid Entry.")



def pe(pl):
    print(pl)

def plll(pe):
    print(pe)

print("1 for pe ")
print("2 for pl ")

choice = input("Please enter: ")

{
    '1': plll(choice),
    '2': pe(choice)
}.get(choice)