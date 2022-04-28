'''
Zadanie 2.2 Trójki Pitagorejskie
Wygeneruj trójki (tuple trzyelementowe) liczb całkowitych a b c, które tworzą trójkąt
pitagorejski (czyli a² + b² = c²), ale bez powtórzeń i tylko takich, że a < b < c, dla liczb do
podanego zakresu (np. 1000). Postaraj się zrobić to za pomocą wyrażenia listotwórczego.
Istnieją tu rozwiązania bardziej i mniej wydajne ;-) – do przemyślenia.
'''

def trójki_pitagorejskie(n):
    # wersja 1 - pętle
    # zbior = []
    # for a in range(n-1):
    #     for b in range (a+1, n):
    #         for c in range(b+1, n+1):
    #             if a*a + b*b == c*c:
    #                 zbior.append((a, b, c))
    # return zbior
    '''
    wersja 2 - wyrazenie listotwórcze
    :param n: przeszukiwany zakres liczb
    :return: listę tupli liczb tworzacych trójkąty pitagorejskie
    '''
    return [(a, b, c) for a in range(n-1) for b in range(a+1, n) for c in range(b+1, n+1) if a*a + b*b == c*c ]

def trójki_pitagorejskie1(n):
    zbior = []
    for a in range(1,n//3):
        print(a)
        for b in range(a+1, n//2):
            c = n - a - b
            if a*a + b*b == c*c:
                print(f'{a}, {b}, {c}')
                zbior.append((a, b, c))
    return zbior



def main():
    print('Trójki Pitagorejskie')
    while True:
        try:
            liczba = input('podaj liczbę większą od 0 (koniec - pusty ciąg): ')
            if liczba == '':
                break
            elif int(liczba) >= 1:
                print(trójki_pitagorejskie1(int(liczba)))
            else:
                print('możliwe tylko liczby całkowite większe od 0')
        except Exception as e:
            print(e)


if __name__ == '__main__':
   main()