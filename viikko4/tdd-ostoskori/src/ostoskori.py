from ostos import Ostos
from tuote import Tuote

class Ostoskori:
    def __init__(self):
        self._ostokset: dict[Tuote, Ostos] = {}

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self._ostokset.values())

    def hinta(self):
        return sum(ostos.hinta() for ostos in self._ostokset.values())

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava in self._ostokset:
            self._ostokset[lisattava].muuta_lukumaaraa(1)
        else:
            self._ostokset[lisattava] = Ostos(lisattava)   

    def poista_tuote(self, poistettava: Tuote):
        if self._ostokset[poistettava].lukumaara() > 1:
            self._ostokset[poistettava].muuta_lukumaaraa(-1)
        else:
            del self._ostokset[poistettava]

    def tyhjenna(self):
        self._ostokset = {}

    def ostokset(self):
        return list(self._ostokset.values())
