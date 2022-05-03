'''
Zadanie 2.4 Klasa dla ułamków
Stwórz klasę, której obiekty reprezentują liczby wymierne w postaci ułamkowej. Klasa powinna
implementować dokładne operacje na ułamkach (nie poprzez konwersję na float). Podobnie
jak robiliśmy z Vectorem, utwórz klasę, która zwraca nowe obiekty jako wyniki swoich operacji.
Nie dopuszczaj do sytuacji, aby w mianowniku znalazło się zero – wyrzucaj wyjątek, a także
utrzymuj mianownik dodatni (gdy ktoś próbuje podać ujemny, to wpisz dodatni i zamień znak
licznika). Operacje arytmetyczne powinny zwracać wynik w postaci maksymalnie skróconej.
Proponowane elementy klasy:
• tworzenie: Fraction(nominator=0, denominator=1)
• atrybuty nominator, denominator dają wartość licznika i mianownika
• __str__ , __repr__
• operacje matematyczne + - * / za pomocą magicznych metod __add__, __sub__ itd.
• porównania == != < <= > >= działające w oparciu o wartości, ale bez wyliczania floatów,
• __float__ i __int__ – konwersja na typ float (z maksymalną precyzją)
i int (część całkowita)
• __bool__ – zwraca True jeśli licznik nie jest zerem
Metody zwracające wyniki – można je oznaczyć jako @property
• shortened() – zwraca ułamek o tej samej wartości, skrócony w miarę możliwości
(o największy wspólny dzielnik licznika i mianownika)
• reciprocal() – zwraca odwrotność ułamka (nowy obiekt)
Wraz z dodawaniem kolejnych metod, testuj je za pomocą pytest.
'''

from ulamek import *

def main():
    try:
        u1 = Ulamek(3, 4)
        u2 = Ulamek(2, 6)
        u3 = Ulamek(1, 2)
        u4 = Ulamek(1, 0)
    except Exception as e:
        print(e)

    if u4:
        print('jest')
    else:
        print('nie')

    print(u1)
    print(u2)
    u2.skroc()
    print(u2)
    print(u3)
    u3.odwrotnosc()
    print(u3)

    print(f'+ {u1+u2}')
    print(f'- {u1-u2}')
    print(f'* {u1*u2}')
    print(f'/ {u1/u2}')
    print(u1.float())


if __name__ == "__main__":
   main()

