'''
Pan Tadeusz
Napisz zestaw programów, które analizują wskazany plik tekstowy, np. plik
pan-tadeusz.txt. W większości przypadków trzeba plik podzielić na słowa, do czego można
użyć takich technik jak metoda split albo wyrażenia regularne.
'''

def wczytaj_plik(sciezka):
    '''
    wczytanie danych z pliku .txt
    :param sciezka: ścieżka do pliku
    :return: lista obiektów Transakcja
    '''

    znaki_specjalne = {'—', '.', ',', ':', ';', '(', ')', '!', '...', '…', '«', '»', ';', '*', '?'}
    with open(sciezka, mode='r', encoding='utf-8') as plik:
        tresc = plik.read()

    tresc = tresc.replace('\n',' ')
    for znak in znaki_specjalne:
        tresc = tresc.replace(znak, '')

    return tresc.split(' ')

import locale

locale.setlocale(locale.LC_ALL, 'Polish')
def wczytaj_plik_posortowany(sciezka):
    znaki_specjalne = {'—', '.', ',', ':', ';', '(', ')', '!', '...', '…', '«', '»', ';', '*', '?'}
    with open(sciezka, mode='r', encoding='utf-8') as plik:
        tresc = plik.read()

    tresc = tresc.replace('\n',' ')
    for znak in znaki_specjalne:
        tresc = tresc.replace(znak, '')

    tresc_posortowana = tresc.split(' ')
    tresc_posortowana.sort(key=locale.strxfrm)

    return tresc_posortowana
