#!/usr/bin/env python3
"""Ciddi testler. Ciddi olmayan iddialar."""

import unittest

from kumanda_kurtar import kurtarma_olasiligi, raporla, rot13


class TestTim(unittest.TestCase):
    def test_aralik(self):
        p = kurtarma_olasiligi(12, 3, 10, 0.4, False)
        self.assertGreater(p, 0)
        self.assertLess(p, 1)

    def test_kedi_kotulestirir(self):
        yalin = kurtarma_olasiligi(10, 2, 5, 0.2, False)
        kedili = kurtarma_olasiligi(10, 2, 5, 0.2, True)
        self.assertLess(kedili, yalin)

    def test_derin_daha_zor(self):
        sig = kurtarma_olasiligi(3, 1, 1, 0.1, False)
        derin = kurtarma_olasiligi(40, 1, 1, 0.1, False)
        self.assertGreater(sig, derin)

    def test_rapor_damgali(self):
        metin = raporla(8, 2, 4, 0.3, False)
        self.assertIn("DAMGA", metin)
        self.assertIn("Kayyum Grok", metin)

    def test_rot13_tersinir(self):
        self.assertEqual(rot13(rot13("merhaba")), "merhaba")


if __name__ == "__main__":
    unittest.main()
