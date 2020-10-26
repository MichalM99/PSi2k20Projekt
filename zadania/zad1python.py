
#3
#Old
print('%10s' % ('test',))
#New
print('{:>5}'.format('test'))
#Old
print('%.5s' % ('Moszczyński',))
#New
print('{:.7}'.format('Moszczyński'))
#Old
print('%f' % (3.141592653589793))
#New
print('{:f}'.format(3.141592653589793))
#Old
print('%+d' % (42,))
#New
print('{:+d}'.format(42))
#Old
data = {'first': 'Michal', 'last': 'Moszczyński'}
print('%(first)s %(last)s' % data)
#New
print('{first} {last}'.format(**data))


"""
#Zad1
f = open('zad1tekstlorem.txt')
text = f.read()
#Zad2
imie = "Michal"
nazwisko = "Moszczynski"
nazwisko = nazwisko[:3]
imie = imie[:2]
#print("Lubię język {1} oraz {0}".format("Java", "Python"))
print("W tekscie jest {0} liter {1}, {2} liter {3}, {4} liter {5}, {6} liter {7}".format(text.count(imie[0]), imie[0]
                                                                                         , text.count(imie[1]), imie[1],
                                                                                         text.count(nazwisko[1]), nazwisko[1],
#3

#4
print(dir("Ala ma kota, a kot ma Alicje"))
help("Ala ma kota, a kot ma Alicje".strip())
#Zad5
imnazw = "Michał Moszczyński"
print(imnazw[::-1])
                                                                                         text.count(nazwisko[2]), nazwisko[2]))
#Zad6
lista1 = list(range(1,11))
lista2 = lista1[5:]
lista1 = lista1[:5]
print(lista1)
print(lista2)
#Zad7
lista1 = list(range(1,11))
lista2 = lista1[5:]
lista1 = lista1[:5]
lista3 = lista1 + lista2
lista3.insert(0,0)
print(lista3[::-1])
#Zad8
krotka = ((135435,"Jacek Czarodziej"),(543654,"Krzysztof Witam"),(542752, "Arnold Kowalski"))
print(krotka)
#Zad9
slownik = dict(krotka)
print(slownik)
#Zad10
numery = ("531645325","547385375","427542864", "572753574", "531645325","547385375")
numerybezpowt = set(numery)
print(numerybezpowt)
#Zad11
for i in range(1,11):
    print(i)
#Zad12
for i in range(100,19,-1):
    print(i)
#13
slownik1 = dict([("jeden", 1), ("dwa", 2), ("trzy", 3)])
slownik2 = dict([("Michał", "M"), ("Krzysiek", "K"),("Arnold", "A")])
lista = [slownik1, slownik2]
def program(lista):
    tekst = "W tekscie sa dwa slowniki" + str(lista[0]) + " oraz " + str(lista[1]) + "\nZawartosc pierwszego: "
    for i in lista[0]:
        tekst+= i + " "
    tekst+= "\nZawartosc drugiego: "
    for i in lista[1]:
        tekst+= i + " "
    print(tekst)
program(lista)
"""

