'''
Zadanie 2.3 Analiza danych "sprzedaż"
W pliku sprzedaz.csv znajdują się dane opisujące sprzedaż różnych sklepów - w każdej linii jest
jedna transakcja. Cena jest ceną jednostkową, a w osobnej kolumnie jest podana liczba sztuk.
Dopiero ich iloczyn jest wartością transakcji – trzeba to liczyć w programie.
Napisz programy, które czytają dane z tego pliku i obliczają:
1. Sumę oraz średnią wartości wszystkich transakcji z całego pliku.
2. Ilość, sumę oraz średnią wartość transakcji z wybranego miasta (niech program pyta o
nazwę miasta na początku).
3. Dla każdego miasta występującego w pliku – sumę transakcji z tego miasta (wypisać bez
powtórzeń).
'''

from transakcja import *
from collections import defaultdict


def wczytaj_plik(sciezka):
    '''
    wczytanie danych z pliku .csv
    :param sciezka: ścieżka do pliku
    :return: lista obiektów Transakcja
    '''
    with open(sciezka, mode='r', encoding='utf-8') as plik:
        plik.readline()
        lista = []
        for linia in plik:
            t = linia.split(';')
            trans = Transakcja(t[0], t[1], t[2], t[3], t[4], t[5], float(t[6]), float(t[7]))
            lista.append(trans)
    return lista


def suma_transakcji(lista_transakcji):
    '''
    wyliczenie sumy wszystkich transakcji
    :param lista_transakcji:
    :return: suma transakcji
    '''
    suma = 0
    for t in lista_transakcji:
        suma += t.wartosc_transakcji
    return suma


def licznik_transakcji_miasto(lista_transakcji, jakie_miasto):
    '''
    wyliczenie ilości, sumy oraz średniej ilości transakcji dla wybranego miasta
    :param lista_transakcji:
    :param jakie_miasto:
    :return: ilość, suma, śrenia transakcji dla wybranego miasta
    '''
    ilosc = 0
    suma = 0
    for t in lista_transakcji:
        if (t.miasto).upper() == jakie_miasto.upper():
            ilosc += 1
            suma += t.wartosc_transakcji
    srednia = suma / ilosc
    return (ilosc, suma, srednia)


def wyswietl_info_dla_miasta(lista_transakcji):
    miasta = set()
    for t in lista_transakcji:
        miasta.add((t.miasto).upper())

    print(miasta)
    jakie_miasto = ''

    while jakie_miasto not in miasta:
        jakie_miasto = input('podaj nazwę miasta: ').upper()

    ilosc_transakcji, suma_transakcji, srednia_transakcji = licznik_transakcji_miasto(lista_transakcji, jakie_miasto)
    print(f'ilosc transakcji: {ilosc_transakcji:.2f}')
    print(f'suma transakcji: {suma_transakcji:.2f}')
    print(f'srednia transakcji: {srednia_transakcji:.2f}')


def suma_dla_miast(lista_transakcji):
    miasta = defaultdict(float)

    for t in lista_transakcji:
        miasta[t.miasto] += t.wartosc_transakcji
    return miasta


def main():
    transakcje = wczytaj_plik('sprzedaz.csv')

    print('Wczytane rekordy: ', len(transakcje))
    for tran in transakcje:
        print(tran)
    print(50 * '-')

    # 1. Sumę oraz średnią wartości wszystkich transakcji z całego pliku.
    print(f'suma wszystkich transakcji: {suma_transakcji(transakcje):.2f}')
    srednia_wszystkich_transakcji = suma_transakcji(transakcje) / len(transakcje)
    print(f'średnia dla wszystkich transakcji: {srednia_wszystkich_transakcji:.2f}')
    print(50 * '-')

    # 2. Ilość, sumę oraz średnią wartość transakcji z wybranego miasta (niech program pyta o
    # nazwę miasta na początku).
    wyswietl_info_dla_miasta(transakcje)
    print(50 * '-')

    # 3. Dla każdego miasta występującego w pliku – sumę transakcji z tego miasta (wypisać bez
    # powtórzeń).
    miasta = suma_dla_miast(transakcje)
    for miasto in miasta:
        print(f'{miasto:25} - {miasta[miasto]: 12.2f}')


if __name__ == '__main__':
    main()
