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
            trans = Transakcja(t[0], t[1], t[2], t[3], t[4], t[5], float(t[6]), float(t[7]), float(t[6])*float(t[7]))
            lista.append(trans)
    return lista

def suma_transakcji(lista_transakcji):
    suma = 0
    for t in lista_transakcji:
        suma += t.wartosc_transakcji
    return suma

def main():
    transakcje = wczytaj_plik('sprzedaz.csv')
    print('Wczytane rekordy: ', len(transakcje))
    for tran in transakcje:
        print(tran)

    print(f'suma: {suma_transakcji(transakcje):.2f}')


if __name__ == '__main__':
    main()