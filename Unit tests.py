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
        result= Backend.build_successor_tables("TAGCCAT","AGTGCAC")
        #then
        self.assertEqual(result, expected)
    def test_build_successor_tables2(self):
        # given
        seqA="AGCA"
        seqB="AGAAG"
        expected=([[1,4,4,4,-1],[2,2,-1,-1,-1],[3,3,3,-1,-1]],[[1,3,3,4,-1,-1],[2,2,5,5,5,-1],[-1,-1,-1,-1,-1,-1]],3)
        # when
        result= Backend.build_successor_tables("AGCA","AGAAG")
        #then
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
