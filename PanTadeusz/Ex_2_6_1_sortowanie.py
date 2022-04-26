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
    slowa_pan_tadeusz = wczytaj_plik('pan-tadeusz.txt')

    licznik_malych_slow = policz_wszystkie_male_slowa(slowa_pan_tadeusz)

    lista_slow_alfab = sorted(licznik_malych_slow.items(), key=operator.itemgetter(0))
    posortowane_alfab = dict(lista_slow_alfab)

    for slowo in posortowane_alfab:
        print(f'{slowo:30} -> {posortowane_alfab[slowo]:10}')

    lista_slow_ilosc = sorted(licznik_malych_slow.items(), key=operator.itemgetter(1))
    posortowane_ilosc = dict(lista_slow_ilosc)

    for slowo in posortowane_ilosc:
        print(f'{slowo:30} -> {posortowane_ilosc[slowo]:10}')


if __name__ == '__main__':
    main()