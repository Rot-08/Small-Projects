from glob import escape
from locale import currency


class TemperatureConverter():

    def fahrenheitToCelcius(temp):
        return((5/9) * (temp - 32))

    def celciusToFahrenheit(temp):
        return((9/5 * temp) + 32)


class DistanceConverter():
    def milesToKm(miles):
        return (miles * 1.60934)

    def kmToMiles(km):
        return (km * 0.621371)
    
    def footToMeters(foot):
        return (foot * 0.3048)
    
    def metersToFoot(meters):
        return (meters * 3.28084)

    def yardToMeters(yard):
        return (yard * 0.9144)

    def metersToYards(meters):
        return ( meters * 1.09361)
    
    def cmToInch(cm):
        return (cm * 0.39370)
    
    def inchtoCm(inch):
        return (inch * 2.54)


class CurrencyConverter():
    def nairaToDollar(naira):
        return (naira * 0.0016666666666)

    def dollarToNaira(dollar):
        return (dollar * 600)


class MassConverter():
    def kgToPound(kg):
        return (kg * 2.20462)
    
    def poundToKg(pound):
        return (pound * 0.453592)

    def gramToOunce(kg):
        return (kg * 0.035274)

    def OunceToGram(ounce):
        return (ounce * 28.3495)


Distance = {'submenu': ['Miles to Km', "Km to Miles", "Yard To meter", 'Meter to Yard', "Foot To Meter", "Meter to Foot", "Cm to Inch", "Inch To Cm"], "preamble": "Choose The Units "}
Currency= {'submenu': ['Naira To Dollar', 'Dollar To Naira'], "preamble": "Choose The currency "}
Mass = {'submenu': ['Pound To Kg', "Kg to Pound", 'Gram To Ounce', "ounce To Gram"], "preamble": "Choose The Units "}
Temperature = {'submenu': ['Fahrenheit To celcius', "Celcius To Fahrenheit"], "preamble": "Choose The Units "}


MainMenu = {"submenu": ['Temperature', 'Distance', "Currency", "Mass"], 'preamble': "What do you wish to convert? ",  "submenus": [Temperature, Distance, Currency, Mass]}

def showMenu(menu):
    try:
        print(menu["preamble"])
        for index, item in enumerate(menu['submenu']):
            print("{index}. {item}".format(index = index+1, item = item))
        
        choice = int(input(" Please Choose From numbers provided: "))
        choice -= 1
        return menu['submenus'][choice]
    except:
        print("Invalid Entry.")
        


def submenu(menu):
    try:
        print(menu["preamble"])
        for index, item in enumerate(menu['submenu']):
            print("{index}. {item}".format(index = index+1, item = item))
    
        choice = int(input("\n Please Choose From numbers provided: "))
        choice -= 1
        print(menu["submenu"][choice])
        return(menu["submenu"][choice])

    except:
        print("Invalid Entry.")


try:
    selection = submenu(showMenu(MainMenu))
    number = int(input("Number Of Units To convert: "))
except:
    print("Invalid Units")

dicta = {
    'Fahrenheit To celcius': TemperatureConverter.fahrenheitToCelcius(number), 
    "Celcius To Fahrenheit": TemperatureConverter.celciusToFahrenheit(number), 

    'Miles to Km': DistanceConverter.milesToKm(number), 
    "Km to Miles": DistanceConverter.kmToMiles(number), 
    "Yard To meter":DistanceConverter.yardToMeters(number), 
    'Meter to Yard':DistanceConverter.metersToYards(number), 
    "Foot To Meter":DistanceConverter.footToMeters(number), 
    "Meter to Foot":DistanceConverter.metersToFoot(number), 
    "Cm to Inch":DistanceConverter.cmToInch(number),
    "Inch To Cm":DistanceConverter.inchtoCm(number),


    'Naira To Dollar': CurrencyConverter.nairaToDollar(number),
    'Dollar To Naira'  : CurrencyConverter.dollarToNaira(number),

    'Pound To Kg': MassConverter.kgToPound(number), 
    "Kg to Pound": MassConverter.poundToKg(number), 
    'Gram To Ounce': MassConverter.gramToOunce(number), 
    "ounce To Gram": MassConverter.OunceToGram(number)
}
print("Result:", end = "\t")
print(dicta[selection])