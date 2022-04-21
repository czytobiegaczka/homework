'''
3. czy_pierwsza(liczba)
Sprawdza czy liczba jest pierwsza i zwraca True albo False.
'''

def czy_pierwsza(liczba):
    if liczba == 1 or liczba == 2:
        return True
    else:
        for count in range(2, liczba):
            if liczba % count == 0:
                return False
        return True

def main():
    print('LICZBA PIERWSZA?')
    while True:
        try:
            liczba = input('podaj liczbę większą od 0 (koniec - pusty ciąg): ')
            if liczba == '':
                break
            if int(liczba) >= 1:
                if czy_pierwsza(int(liczba)):
                    print(f'{liczba} - jest liczbą pierwszą')
                else:
                    print(f'{liczba} - nie jest liczbą pierwszą')
        except Exception as e:
            print('dozwolone tylko liczby calkowite wieksze od 1')


if __name__ == '__main__':
   main()