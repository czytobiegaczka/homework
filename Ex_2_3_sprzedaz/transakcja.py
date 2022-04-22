class Transakcja:
    '''
    obiekt tej klasy reprezentuje jedną transakcję
    '''
    def __init__(self, id, data, miasto, sklep, kategoria, towar, cena, sztuk, wartosc_transakcji) :
        self.id = id
        self.data = data
        self.miasto = miasto
        self.sklep = sklep
        self.kategoria = kategoria
        self.towar = towar
        self.cena = cena
        self.sztuk = sztuk
        self.wartosc_transakcji = wartosc_transakcji

    def __str__(self):
        return f'{self.id} {self.data} {self.miasto} {self.sklep} {self.kategoria} {self.towar} {self.cena} {self.sztuk} {self.wartosc_transakcji}'

