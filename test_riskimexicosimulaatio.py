import unittest
from unittest.mock import patch
from riskimexicosimulaatio import heita, lisaaListaan, pelaa

class TestRiskiMexico(unittest.TestCase):

    def test_lisaaListaan(self):
        lista1 = [[61,0], [62,0], [21,0]]
        lista2 = [0,0,0]

        lisaaListaan(lista1, [33,3])
        lisaaListaan(lista2, [33,3])
        self.assertListEqual(lista1, [[33,3],[61,0], [62,0]])
        self.assertListEqual(lista2, [[33,3],0,0])


    def test_heitaRajat(self):
        alarajaTulos = 1
        ylarajaTulos = 6
        alarajaHeitot = 0
        ylarajaHeitot = 6
        
        for i in range(100000):
            tulos = heita()
            noppa1, noppa2 = divmod(tulos[0], 10)
            self.assertTrue(alarajaTulos <= noppa1 <= ylarajaTulos, f"{noppa1} ei ollut rajojen sisällä")
            self.assertTrue(alarajaTulos <= noppa2 <= ylarajaTulos, f"{noppa2} ei ollut rajojen sisällä")
            self.assertTrue(alarajaHeitot <= tulos[1] <= ylarajaHeitot, f"{tulos[1]} ei ollut rajojen sisällä")



    @patch('random.randint', side_effect=[1,1,2,2,3,3,4,4,5,5,6,6]) 
    def test_heitaHeittojaJaljellaParit(self, mock_randint):
        tulos1 = heita()
        tulos2 = heita()
        tulos3 = heita()
        tulos4 = heita()
        tulos5 = heita()
        tulos6 = heita()

        self.assertEqual(tulos1[0], tulos1[1] * 10 + tulos1[1])
        self.assertEqual(tulos2[0], tulos2[1] * 10 + tulos2[1])
        self.assertEqual(tulos3[0], tulos3[1] * 10 + tulos3[1])
        self.assertEqual(tulos4[0], tulos4[1] * 10 + tulos4[1])
        self.assertEqual(tulos5[0], tulos5[1] * 10 + tulos5[1])
        self.assertEqual(tulos6[0], tulos6[1] * 10 + tulos6[1])

        
    @patch('random.randint', side_effect=[1,2,1,3,1,4,1,5,1,6,2,3,2,4,2,5,2,6,3,4,3,5,3,6,4,5,4,6,5,6]) 
    def test_heitaHeittojaJaljellaMuut(self, mock_randint):
        tulos1 = heita()
        tulos2 = heita()
        tulos3 = heita()
        tulos4 = heita()
        tulos5 = heita()
        tulos6 = heita()
        tulos7 = heita()
        tulos8 = heita()
        tulos9 = heita()
        tulos10 = heita()
        tulos11 = heita()
        tulos12 = heita()
        tulos13 = heita()
        tulos14 = heita()
        tulos15 = heita()

        self.assertEqual(tulos1[1], 0)
        self.assertEqual(tulos2[1], 0)
        self.assertEqual(tulos3[1], 0)
        self.assertEqual(tulos4[1], 0)
        self.assertEqual(tulos5[1], 0)
        self.assertEqual(tulos6[1], 0)
        self.assertEqual(tulos7[1], 0)
        self.assertEqual(tulos8[1], 0)
        self.assertEqual(tulos9[1], 0)
        self.assertEqual(tulos10[1], 0)
        self.assertEqual(tulos11[1], 0)
        self.assertEqual(tulos12[1], 0)
        self.assertEqual(tulos13[1], 0)
        self.assertEqual(tulos14[1], 0)
        self.assertEqual(tulos15[1], 0)


    @patch('random.randint', side_effect=[1,2,
                                          1,1,3,1,
                                          1,1,2,1,
                                          5,2,2,2,2,1,3,1,
                                          5,4,5,4,5,4,2,2,2,1,3,1,
                                          4,4,2,1,2,1,2,1,3,1,
                                          5,5,2,1,2,2,3,1,3,1,3,1,2,1,3,1]) 
    def test_pelaa(self, mock_randint):
        tulos1 = pelaa() #Suora mexico
        tulos2 = pelaa() #11 ja pois
        tulos3 = pelaa() #1,1,2,1 pari, mexicolla pois
        tulos4 = pelaa() #5,2,2,2,2,1,3,1 -- Tyhjää, parilla peliin, mexico, ja pois
        tulos5 = pelaa() #5,4,5,4,5,4,2,2,2,1,3,1 -- Kolme samaa (mexico), parilla peliin, mexico ja pois
        tulos6 = pelaa() #4,4,2,1,2,1,2,1,3,1 -- parilla peliin, 3 mexicoa, pois
        tulos7 = pelaa() #5,5,2,1,2,2,3,1,3,1,3,1,2,1,3,1-- parilla peliin, 1 mexico, pari, kolme samaa, mexico, pois

        self.assertEqual(tulos1, 1)
        self.assertEqual(tulos2, 0)
        self.assertEqual(tulos3, 1)
        self.assertEqual(tulos4, 1)
        self.assertEqual(tulos5, 2)
        self.assertEqual(tulos6, 4)
        self.assertEqual(tulos7, 3)



if __name__ == '__main__':
    unittest.main()