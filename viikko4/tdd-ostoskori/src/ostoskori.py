from ostos import Ostos
from tuote import Tuote

class Ostoskori:
    def __init__(self):
        self._tuotteet = []

    def tavaroita_korissa(self):
        return len(self._tuotteet)

    def hinta(self):
        return sum(tuote.hinta() for tuote in self._tuotteet)

    def lisaa_tuote(self, lisattava: Tuote):
        self._tuotteet.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        pass

    def tyhjenna(self):
        pass

    def ostokset(self):
        return self._tuotteet
