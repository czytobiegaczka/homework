'''
2.6.1 * Sortowanie
Sprowadzaj wszystkie słowa do małych liter i licz jednolicie bez podziału na małe i duże litery.
Posortuj wypisywane wyniki na dwa sposoby:
a) alfabetycznie
b) według liczby wystąpień.
'''

import operator

from pantadeusz import *
from collections import *


def policz_wszystkie_male_slowa(tresc):
    slowa = defaultdict(int)
    for wyraz in tresc:
        if wyraz != '':
            slowa[wyraz.lower()] += 1
    return slowa

def main():
    slowa_pan_tadeusz = wczytaj_plik_posortowany('pan-tadeusz.txt')

    print('Posortowany alfabetycznie licznik małych słów: ')

    for slowo, ilosc in policz_wszystkie_male_slowa(slowa_pan_tadeusz).items():
        print(f'{slowo:30} -> {ilosc:10}')

    print('Posortowany wg liczby wystąpień licznik małych słów: ')

    lista_slow_ilosc = sorted(policz_wszystkie_male_slowa(slowa_pan_tadeusz).items(), key=operator.itemgetter(1))

    for slowo, ilosc in dict(lista_slow_ilosc).items():
        print(f'{slowo:30} -> {ilosc:10}')


if __name__ == '__main__':
    main()