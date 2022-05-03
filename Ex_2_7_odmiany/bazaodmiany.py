from collections import defaultdict



class BazaOdmiany:
    def __init__(self, odmiany):
        self.odmiany = odmiany

    def wczytaj(zrodlo):
        with open(zrodlo, mode='r', encoding='utf-8') as plik:
            lista_podstaw = defaultdict(list)
            for linia in plik:
                o = linia.split('\t')
                # odm = BazaOdmiany(o[0], o[1], o[2], o[3])
                lista_podstaw[o[1]].append(o[0])
            odm = BazaOdmiany(lista_podstaw)
        return odm






