def nwd_liczb(licz1, licz2):
    while licz2:
        liczba = licz1
        licz1 = licz2
        licz2 = liczba % licz2
    return licz1


class Ulamek:
    def __init__(self, licznik=0, mianownik=1):
        if mianownik == 0:
            raise ValueError('mianownik nie może mnieć wartości 0')
        self.licznik = licznik
        self.mianownik = mianownik

    def __str__(self):
        return f'{self.licznik}/{self.mianownik}'

    def __repr__(self):
        return f'Ulamek(licznik={self.licznik}, mianownik={self.mianownik})'

    # operacje matematyczne

    def __add__(self, other):
        '''
        dodawanie ułamków
        :param other: obiekt typu ułamek
        :return: obiekt typu ułamek- suma ułamków
        '''
        licznik1 = self.licznik * other.mianownik
        licznik2 = other.licznik * self.mianownik
        mianownik = self.mianownik * other.mianownik

        ulamek_wynik = Ulamek(licznik1 + licznik2, mianownik)
        ulamek_wynik.skroc()
        return ulamek_wynik

    def __sub__(self, other):
        '''
        odejmowanie ułamków
        :param other: obiekt typu ułamek
        :return: obiekt typu ułamek- różnica ułamków
        '''
        licznik1 = self.licznik * other.mianownik
        licznik2 = other.licznik * self.mianownik
        mianownik = self.mianownik * other.mianownik

        ulamek_wynik = Ulamek(licznik1 - licznik2, mianownik)
        ulamek_wynik.skroc()
        return ulamek_wynik

    def __mul__(self, other):
        '''
        mnożenie ułamków
        :param other: obiekt typu ułamek
        :return: obiekt typu ułamek- iloczyn ułamków
        '''
        ulamek_wynik = Ulamek(self.licznik * other.licznik, self.mianownik * other.mianownik)
        ulamek_wynik.skroc()
        return ulamek_wynik

    def __truediv__(self, other):
        '''
        dzielenie ułamków
        :param other: obiekt typu ułamek
        :return: obiekt typu ułamek- iloraz ułamków
        '''
        ulamek_wynik = Ulamek(self.licznik * other.mianownik, self.mianownik * other.licznik)
        ulamek_wynik.skroc()
        return ulamek_wynik

    def __bool__(self):
        '''
        sprawdza czy liczby mogą tworzyć ułmek
        :param other: obiekt typu ułamek
        :return: True / False
        '''
        if self.mianownik == 0:
            return False
        else:
            return True

    @property
    def __float__(self):
        return self.licznik / self.mianownik

    def skroc(self):
        nwd = nwd_liczb(self.licznik, self.mianownik)
        self.licznik //= nwd
        self.mianownik //= nwd

    def odwrotnosc(self):
        licznik = self.licznik
        mianownik = self.mianownik
        self.licznik = mianownik
        self.mianownik = licznik
