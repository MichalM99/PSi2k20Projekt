




"""
#1
def fun1(a_list, b_list):
    wynik = []
    i = 0
    for i in range(0, len(a_list), 2):
        wynik.append(a_list[i])
    for i in range(1, len(b_list),2):
        wynik.insert(i, b_list[i])
    return wynik


a = [84, 64, 54, 65, 23, 65]
b = [76, 43, 765, 543, 764, 90]
print(a,b)
print(fun1(a,b))
#2
def fun2(text_data):
    length = len(text_data)
    letters = list(a)
    big_letters = a.upper()
    small_letters = a.lower()
    dict = {length : letters, big_letters : small_letters}
    return dict


#3
def fun3(text, letter):
    wynik = text.replace(letter, '')
    return wynik
#4
def fun4(temperatureC, temperature_type):
    if temperature_type=="Fahrenheit":
        return (temperatureC * 1.8) +32
    elif temperature_type=="Rankine":
        return (temperatureC + 273.15) * 1.8
    elif temperature_type=="Kelvin":
        return temperatureC + 273.15
#5
class Kalkulator:
    def add(a, b):
        return a+b
    def multiply(a, b):
        return a * b
    def divide(a,b):
        return a / b
    def difference(a,b):
        return a - b


#6
class ScienceCalculator(Kalkulator):
    def potegowanie(a, b):
        return a ** b
#7
def fun7(text):
        print(text[::-1])

fun7("ala ma kota")
#8 i 9
from file_manager import FileManager
pojazd = FileManager('abc.txt')
pojazd.read_file()
pojazd.update_file("witam witam")
pojazd.read_file()

#10
#-
"""