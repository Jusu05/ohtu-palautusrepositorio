import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42
        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            return {1: 10, 2: 5}[tuote_id]

        def varasto_hae_tuote(tuote_id):
            return {1: Tuote(1, "maito", 5), 2: Tuote(2, "keksi", 1)}[tuote_id]

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.pankki_mock = pankki_mock
        self.varasto_mock = varasto_mock
        self.kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_oikeilla_parametreilla_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 5)

    def test_maksettaessa_kahden_tuoteen_ostos_pankin_metodia_tilisiirto_oikeilla_parametreilla_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 6)

    def test_maksettaessa_kahden_saman_tuoteen_ostos_pankin_metodia_tilisiirto_oikeilla_parametreilla_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 10)

    def test_tilimaksu_veloittaa_vain_varastossa_olevan_tuotteen_hinnan(self):
        self.varasto_mock.saldo.side_effect = lambda tuote_id: {1: 10, 2: 0}[tuote_id]
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self.kauppa._kaupan_tili, 5)
