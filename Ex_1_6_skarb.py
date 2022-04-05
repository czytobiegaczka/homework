'''
Zadanie 1.6 Skarb
Napisz grę tekstową polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o
rozmiarach 10 na 10. Program na początku losuje pozycję skarbu oraz pozycję gracza.
Następnie użytkownik może wprowadzać komendy zmieniające położenie postaci o jedną
pozycję w górę/dół/lewo/prawo (np zgodnie z konwencją WSAD) – normalnie za pomocą input.
Gdy gracz wejdzie na pole, na którym kryje się skarb – wygrywa.
Gdy wyjdzie poza planszę – przegrywa.
Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza w dobrym
kierunku. Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na
dojście do celu.
Dodatkowe utrudnienia, gdy zacznie działać pierwsza wersja:
• Po wykonaniu większej liczby kroków niż dwukrotność minimalnej liczby kroków na
początku, umieść skarb w nowym miejscu (i od nowa zacznij liczyć kroki).
• Z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku.
'''