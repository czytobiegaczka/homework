class Transakcja:
    '''
    obiekt tej klasy reprezentuje jedną transakcję
    '''
    def __init__(self, id, data, miasto, sklep, kategoria, towar, cena, sztuk) :
        self.id = id
        self.data = data
        self.miasto = miasto
        self.sklep = sklep
        self.kategoria = kategoria
        self.towar = towar
        self.cena = cena
        self.sztuk = sztuk

    def __str__(self):
        return f'Transakcja(id={self.id}, data={self.data}, miasto={self.miasto}, sklep={self.sklep}, kategoria={self.kategoria}, towar={self.towar}, cena={self.cena}, sztuk={self.sztuk})'

    @property
    def wartosc_transakcji(self):
        return self.sztuk * self.cena
