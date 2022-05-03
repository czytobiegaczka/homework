'''
Zadanie 2.7 Odmiana słów
Pod adresem zil.ipipan.waw.pl/PoliMorf znajdują się zasoby dotyczące odmiany wyrazów w
języku polskim. Plik PoliMorf-0.6.7.tab (lub nowsza wersja) zawiera relację między
słowem a jego formą podstawową. W pliku tym pierwsza kolumna zawiera słowo być może
odmienione, a druga kolumna zawiera jego formę bazową.
Wczytaj dane z tego pliku do odpowiednich struktur Pythona (list / set / dict) tak, aby dało się
wyszukiwać odmiany dla form podstawowych, a formy podstawowe dla odmian i aby działało to
w przyzwoitym czasie (wczytywanie może chwilę potrwać, ale znalezienie odmiany, gdy dane
są już wczytane, powinno być szybkie – raczej sekunda niż minuta :))
Najporządniej byłoby utworzyć klasę, której obiekt zawiera odpowiednio przygotowaną „bazę
wiedzy” nt. odmiany słów. Obiekt tej klasy tworzy się na podstawie pliku takiego jak
PoliMorf-0.6.7.tab . Obiekt powinien umożliwiać znalezienie formy podstawowej (lub
kilku kandydatów) dla podanego słowa odmienionego oraz odczytanie listy słów odmienionych
na podstawie formy bazowej.
Przykładowe użycie tej klasy mogłoby wyglądać tak (ale szczegóły nie muszą wyglądać
identycznie):
- baza = BazaOdmiany.wczytaj("PoliMorf-0.6.7.tab")
- baza.znajdzFormyPodstawowe("Tadeusza")
[’Tadeusz’]
- baza.znajdzOdmiany("Tadeusz")
[’Tadeusz’, ’Tadeuszowi’, ’Tadeusza’…...
Korzystając z tej klasy napisz program, który w pętli odczytuje od użytkownika kolejne słowa i
dla podanego słowa wyświetla jego formę podstawową lub informację, że nie znaleziono.
Ten sam wyraz może być formą odmienioną dla kilku form bazowych, np. „dam” może
pochodzić od „dać”, ale również od „dama”. Można to uwzględnić we własnym modelu (wersja
zaawansowana) lub upraszczając przyjąć, że wybieracie tylko jedną formę podstawową dla danej
formy odmienionej.
'''

from bazaodmiany import *

def main():
    baza = BazaOdmiany.wczytaj("PoliMorf-0.6.7.tab")
    print('start')
    # for pod, od in baza.items():
    #     print(f'{pod} - {od}')
    print(baza.odmiany)

if __name__ == '__main__':
    main()
