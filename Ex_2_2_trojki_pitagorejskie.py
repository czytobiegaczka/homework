'''
Zadanie 2.2 Trójki Pitagorejskie
Wygeneruj trójki (tuple trzyelementowe) liczb całkowitych a b c, które tworzą trójkąt
pitagorejski (czyli a² + b² = c²), ale bez powtórzeń i tylko takich, że a < b < c, dla liczb do
podanego zakresu (np. 1000). Postaraj się zrobić to za pomocą wyrażenia listotwórczego.
Istnieją tu rozwiązania bardziej i mniej wydajne ;-) – do przemyślenia.
'''

def trójki_pitagorejskie(n):
    pass

def main():
    print('Trójki Pitagorejskie')
    while True:
        try:
            liczba = input('podaj liczbę większą od 0 (koniec - pusty ciąg): ')
            if liczba == '':
                break
            if int(liczba) >= 1:
                if trójki_pitagorejskie(int(liczba)):
                    print(f'{liczba} - jest liczbą pierwszą')
                else:
                    print(f'{liczba} - nie jest liczbą pierwszą')
        except Exception as e:
            print('dozwolone tylko liczby calkowite wieksze od 1')


if __name__ == '__main__':
   main()