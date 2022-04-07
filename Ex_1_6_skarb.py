'''
Zadanie 1.6 Skarb
Napisz grę tekstową polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o
rozmiarach 10 na 10. Program na początku losuje pozycję skarbu oraz pozycję gracza.
Następnie użytkownik może wprowadzać komendy zmieniające położenie postaci o jedną
pozycję w górę/dół/lewo/prawo (np zgodnie z konwencją WSAD) – normalnie za pomocą input.
Gdy gracz wejdzie na pole, na którym kryje się skarb – wygrywa.
Gdy wyjdzie poza planszę – przegrywa.
Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza w dobrym
kierunku. Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na
dojście do celu.
Dodatkowe utrudnienia, gdy zacznie działać pierwsza wersja:
• Po wykonaniu większej liczby kroków niż dwukrotność minimalnej liczby kroków na
początku, umieść skarb w nowym miejscu (i od nowa zacznij liczyć kroki).
• Z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku.
'''

from random import randint


def zmiana_pozycji(pozycja, ruszyl):
    print(pozycja, ruszyl)
    a, b = pozycja
    c, d = ruszyl
    nowa = (a + c, b + d)
    return nowa

print('SKARB')
print('~~~~~\n')

pozycja_skarbu = (randint(1, 10), randint(1, 10))
pozycja_gracza = (randint(1, 10), randint(1, 10))

ruchy = {
    'W': (0, 1),
    'S': (0, -1),
    'A': (-1, 0),
    'D': (1, 0),
}

ilosc_prob = 0

print(pozycja_skarbu)
print(pozycja_gracza)

aktualna_pozycja = pozycja_gracza

print('Zgadnij gdzie jest skarb ?')
print('W - góra \nS - dół \nD - prawo \nA - lewo')
print(f'twoja pozycja: {pozycja_gracza}')

while True:
    ruch = (input('twój ruch: ')).upper()
    if ruch in ruchy:
        ilosc_prob += 1
        nowa_pozycja = zmiana_pozycji(aktualna_pozycja, ruchy[ruch])
        print(nowa_pozycja)
        if nowa_pozycja == pozycja_skarbu:
            print(f'ZWYCIĘSTWO\n dodatłeś do skarbu w {ilosc_prob} krokach')
            break
        aktualna_pozycja = nowa_pozycja

    elif ruch == 'Q':
        break
    else:
        print('to nie jest prawidłowy ruch')
