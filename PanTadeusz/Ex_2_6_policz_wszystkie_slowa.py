'''
Zadanie 2.6 Policz wszystkie słowa
Napisz program, który czyta plik tekstowy i wylicza oraz wypisuje bez powtórzeń wszystkie
słowa występujące w pliku wraz z informacją ile razy dane słowo występuje. Na przykład w ten
sposób (drobny wycinek):
Tace -> 1
Tadeusz -> 107
Tadeusza -> 54
Tadeuszek -> 1
W podstawowej wersji nie przejmuj się kolejnością wypisywanych informacji.
'''
from pantadeusz import *
from collections import *

def policz_wszystkie_slowa(tresc):
    slowa = defaultdict(int)
    for wyraz in tresc:
        if wyraz != '':
            slowa[wyraz] += 1
    return slowa

def main():
    slowa_pan_tadeusz = wczytaj_plik_posortowany('pan-tadeusz.txt')
    # print(slowa_pan_tadeusz)

    licznik_slow = policz_wszystkie_slowa(slowa_pan_tadeusz)
    for slowo in licznik_slow:
        print(f'{slowo:30} -> {licznik_slow[slowo]:10}')

if __name__ == '__main__':
    main()