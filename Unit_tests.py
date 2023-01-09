#W tym pliku znajdują się testy jednostkowe
import unittest
import Backend


class MyTestCase(unittest.TestCase):
    def test_build_successor_tables(self):
        # given
        seqA="TAGCCAT"
        seqB="AGTGCAC"
        expected=([[1, 7, 7, 7, 7, 7, 7, -1],[2, 2, 6, 6, 6, 6, -1, -1],[3, 3, 3, -1, -1, -1, -1, -1],[4, 4, 4, 4, 5, -1, -1, -1]],[[3, 3, 3, -1, -1, -1, -1, -1],[1, 6, 6, 6, 6, 6, -1, -1], [2, 2, 4, 4, -1, -1, -1, -1],[5, 5, 5, 5, 5, 7, 7, -1]],4)
        # when
        result= Backend.build_successor_tables(seqA,seqB)
        #then
        self.assertEqual(result, expected)
    def test_build_successor_tables2(self):
        # given
        seqA="AGCA"
        seqB="AGAAG"
        expected=([[1,4,4,4,-1],[2,2,-1,-1,-1],[3,3,3,-1,-1]],[[1,3,3,4,-1,-1],[2,2,5,5,5,-1],[-1,-1,-1,-1,-1,-1]],3)
        # when
        result= Backend.build_successor_tables(seqA,seqB)
        #then
        self.assertEqual(result, expected)


    def test_pairs(self):
        #given
        MatricesWithRawDim=([[1, 7, 7, 7, 7, 7, 7, -1],[2, 2, 6, 6, 6, 6, -1, -1],[3, 3, 3, -1, -1, -1, -1, -1],[4, 4, 4, 4, 5, -1, -1, -1]],[[3, 3, 3, -1, -1, -1, -1, -1],[1, 6, 6, 6, 6, 6, -1, -1], [2, 2, 4, 4, -1, -1, -1, -1],[5, 5, 5, 5, 5, 7, 7, -1]],4)
        expected = [[0,1,3,0,-1,1],[1,2,1,0,-1,1],[2,3,2,0,-1,1],[3,4,5,0,-1,1]]
        #when
        result = Backend.pairs(MatricesWithRawDim)
        #then
        self.assertEqual(result,expected)
    def test_pairs2(self):
        #given
        MatricesWithRawDim=([[1,4,4,4,-1],[2,2,-1,-1,-1],[3,3,3,-1,-1]],[[1,3,3,4,-1,-1],[2,2,5,5,5,-1],[-1,-1,-1,-1,-1,-1]],3)
        expected=[[0,1,1,0,-1,1],[1,2,2,0,-1,1]]
        #when
        result=Backend.pairs(MatricesWithRawDim)
        # then
        self.assertEqual(result, expected)

    def test_pairs_complete(self):
        #given
        MatricesWithRawDim = ([[1, 7, 7, 7, 7, 7, 7, -1], [2, 2, 6, 6, 6, 6, -1, -1], [3, 3, 3, -1, -1, -1, -1, -1],
                               [4, 4, 4, 4, 5, -1, -1, -1]],
                              [[3, 3, 3, -1, -1, -1, -1, -1], [1, 6, 6, 6, 6, 6, -1, -1], [2, 2, 4, 4, -1, -1, -1, -1],
                               [5, 5, 5, 5, 5, 7, 7, -1]], 4)
        pairsTable = [[0, 1, 3, 0, -1, 1], [1, 2, 1, 0, -1, 1], [2, 3, 2, 0, -1, 1], [3, 4, 5, 0, -1, 1]]
        expected = [[0, 1, 3, 0, -1, 0], [1, 2, 1, 0, -1, 0], [2, 3, 2, 0, -1, 0], [3, 4, 5, 0, -1, 0], [5, 2, 6, 1, 0, 0], [6, 3, 4, 1, 0, 0], [7, 4, 5, 1, 0, 0], [8, 7, 3, 1, 1, 0], [9, 6, 6, 1, 1, 0], [10, 3, 2, 1, 1, 0], [11, 4, 5, 1, 1, 0], [12, 7, 3, 1, 2, 0], [13, 6, 6, 1, 2, 0], [15, 4, 5, 1, 2, 0], [17, 6, 6, 1, 3, 0], [19, 5, 7, 1, 3, 0], [23, 4, 7, 2, 5, 0], [25, 6, 6, 2, 6, 0], [27, 4, 5, 2, 6, 0], [29, 6, 6, 2, 7, 0], [31, 5, 7, 2, 7, 0], [32, 7, 3, 2, 10, 0], [33, 6, 6, 2, 10, 0], [35, 4, 5, 2, 10, 0], [37, 6, 6, 2, 11, 0], [39, 5, 7, 2, 11, 0], [41, 6, 6, 2, 15, 0], [43, 5, 7, 2, 15, 0], [45, 6, 6, 3, 27, 0], [47, 5, 7, 3, 27, 0], [49, 6, 6, 3, 35, 0], [51, 5, 7, 3, 35, 0]]
        #when
        result=Backend.pairs_complete(MatricesWithRawDim, pairsTable)
        #then
        self.assertEqual(result,expected)

    def test_pairs_complete2(self):
        #given
        MatricesWithRawDim=([[1,4,4,4,-1],[2,2,-1,-1,-1],[3,3,3,-1,-1]],[[1,3,3,4,-1,-1],[2,2,5,5,5,-1],[-1,-1,-1,-1,-1,-1]],3)
        pairsTable =[[0,1,1,0,-1,1],[1,2,2,0,-1,1]]
        expected=[[0,1,1,0,-1,0],[1,2,2,0,-1,0],[2,4,3,1,0,0],[3,2,2,1,0,0],[4,4,3,1,1,0],[5,4,3,2,3,0]]
        #when
        result = Backend.pairs_complete(MatricesWithRawDim, pairsTable)
        #then
        self.assertEqual(result, expected)

    def test_LCS(self):
        #given
        seqA="AAAAAAA"
        seqB="AAAAGGGGGGGGGTTTTTTTTTTTTTTCCCCCCCCCCCC"
        expected=['AAAA']
        #when
        result=Backend.LCS(seqA,seqB)
        #then
        self.assertEqual(result,expected)

    def test_LCS2(self):
        #given
        seqA="AGTCCAGAAGTA"
        seqB="GTCCCCTGA"
        expected=['GTCCGA','GTCCTA']
        #when
        result=Backend.LCS(seqA,seqB)
        #then
        self.assertEqual(result,expected)

    def test_LCS3(self): #(nie dziala!)
        #given
        seqA="A"
        seqB="G"
        expected=None
        #when
        result=Backend.LCS(seqA,seqB)
        #then
        self.assertEqual(result,expected)


    def test_LCS4(self): #Czy ta kolejność jest ok?
        # given
        seqA = "TAGCCAT"
        seqB = "AGTGCAC"
        expected = ['TGCA', 'TGCC','AGCA','AGCC']
        # when
        result = Backend.LCS(seqA, seqB)
        # then
        self.assertEqual(result, expected)

        def test_LCS5(self):
            # given
            seqA = ""
            seqB = "GAAA"
            expected = None
            # when
            result = Backend.LCS(seqA, seqB)
            # then
            self.assertEqual(result, expected)

        def test_LCS6(self):
            # given
            seqA = "FGJ"
            seqB = "GAAA"
            expected = None
            # when
            result = Backend.LCS(seqA, seqB)
            # then
            self.assertEqual(result, expected)
        def test_validateAlphabet(self):
            # given
            seqA = "FGJ"
            # then
            with self.assertRaises(ValueError):
                Backend.validateAlphabet(seqA)

        def test_validateEmptySeq(self):
            # given
            seqA = ""
            # then
            with self.assertRaises(ValueError):
                Backend.validateEmptySeq(seqA)

if __name__ == '__main__':
    unittest.main()