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


def plansza(pozycja, symbol):
    x, y = pozycja
    linia = [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    for i in range(11, 1, -1):
        if i != y + 1:
            for znak in linia:
                print(znak, end='')
            print('')
        else:
            linia[x - 1] = symbol
            for znak in linia:
                print(znak, end='')
            linia[x - 1] = ' - '
            print('')


def zmiana_pozycji(pozycja, ruszyl):
    a, b = pozycja
    c, d = ruszyl
    nowa = (a + c, b + d)
    return nowa


def zly_kierunek(poprzednia, aktualna):
    x, y = pozycja_skarbu
    a, b = poprzednia
    c, d = aktualna
    if abs(c - x) > abs(a - x) or abs(d - y) > abs(b - y):
        return True


def wypad_z_planszy(pozycja):
    a, b = pozycja
    if a not in range(1, 11) or b not in range(1, 11):
        return True


pozycja_skarbu = (randint(1, 10), randint(1, 10))
pozycja_gracza = (randint(1, 10), randint(1, 10))

x_s, y_s = pozycja_skarbu
x_g, y_g = pozycja_gracza

droga_minimalna = abs(x_g - x_s) + abs(y_g - y_s)
ilosc_prob = 0

ruchy = {
    'W': (0, 1),
    'S': (0, -1),
    'A': (-1, 0),
    'D': (1, 0),
}
print('\nSKARB')
print('~~~~~\n')
print('Zgadnij gdzie jest skarb ?')
print('W - góra \nS - dół \nA - lewo \nD - prawo\nQ - koniec gry')

plansza(pozycja_gracza, ' X ')
print(f'\ntwoja pozycja: {pozycja_gracza}')

while True:
    ruch = (input('ruch: ')).upper()
    if ruch in ruchy:
        if ilosc_prob < 2 * droga_minimalna:
            ilosc_prob += 1
            nowa_pozycja = zmiana_pozycji(pozycja_gracza, ruchy[ruch])
            if nowa_pozycja == pozycja_skarbu:
                print(f'\nᕦ(ツ)ᕤ ZWYCIĘSTWO\ntwoja pozycja: {nowa_pozycja} - dodatrłeś do skarbu w {ilosc_prob} krokach')
                plansza(pozycja_skarbu, ' 💎 ')
                break
            elif wypad_z_planszy(nowa_pozycja):
                print(f'\n¯\(°_o)/¯ PRZEGRANA\nwypadłeś z planszy')
                break

            if ilosc_prob % 5 != 0:
                if zly_kierunek(pozycja_gracza, nowa_pozycja):
                    plansza(nowa_pozycja, ' X ')
                    print(f'twoja pozycja: {nowa_pozycja} -:-( idziesz w złym kierunku')
                else:
                    plansza(nowa_pozycja, ' X ')
                    print(f'twoja pozycja: {nowa_pozycja} - :-) jesteś coraz bliżej')
            else:
                print('¯\_(ツ)_/¯ - brak podpowiedzi')

            pozycja_gracza = nowa_pozycja
        else:
            print('zbyt duża ilość prób \n¯\_(ツ)_/¯ SKARB trafia w nowe miejsce')
            pozycja_skarbu = (randint(1, 10), randint(1, 10))
            plansza(pozycja_gracza, ' X ')
            x_s, y_s = pozycja_skarbu
            x_g, y_g = pozycja_gracza
            droga_minimalna = abs(x_g - x_s) + abs(y_g - y_s)
            ilosc_prob = 0

    elif ruch == 'Q':
        break
    else:
        print('to nie jest prawidłowy ruch')
