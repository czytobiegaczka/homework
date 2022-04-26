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
        tresc_bez = plik.read()

    # print(tresc_bez)
    tresc_z = tresc_bez.replace('\n', ' ')
    for znak in znaki_specjalne:
        tresc_bez = tresc_z.replace(znak, '')
        tresc_z = tresc_bez
    tresc = tresc_bez
    return tresc.split(' ')


