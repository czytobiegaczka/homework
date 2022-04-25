'''
Zadanie 2.5 Policz wybrane słowo
Program, który pyta użytkownika o słowo i dla podanego słowa liczy ile razy to słowo występuje
w pliku. Przykładowa sesja:
Podaj słowo: Tadeusz
Słowo Tadeusz występuje 107 razy.
'''

from pantadeusz import *

def policz_wybrane_slowo(tresc, slowo):
    licznik = 0
    for wyraz in tresc:
        if wyraz.upper() == slowo.upper():
            licznik +=1
    return licznik


def main():
    slowa_pan_tadeusz = wczytaj_plik('pan-tadeusz.txt')
    # print(slowa_pan_tadeusz)

    szukane_slowo = input('Podaj słowo: ')
    print(f'Słowo {szukane_slowo} występuje {policz_wybrane_slowo(slowa_pan_tadeusz, szukane_slowo)} razy.')



if __name__ == '__main__':
    main()