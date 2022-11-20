# W tym pliku znajduje się nasza implementacja algorytmu FLCS wraz z potrzebnymi funkcjami

def build_successor_tables(seqA, seqB):
    seqAWithSpace = " " + seqA
    n1 = len(seqAWithSpace)
    seqBWithSpace = " " + seqB
    n2 = len(seqBWithSpace)
    distinctLetters = "".join(dict.fromkeys(seqA + seqB))
    m = len(distinctLetters)
    TseqA = [[-1 for col in range(n1)] for row in range(m)]
    TseqB = [[-1 for col in range(n2)] for row in range(m)]
    for i in range(m):
        for j in range(n1):
            TseqA[i][j] = seqAWithSpace.find(distinctLetters[i], j+1)
        for j in range(n2):
            TseqB[i][j] = seqBWithSpace.find(distinctLetters[i], j+1)
    return TseqA, TseqB

def pairs(TseqA, TseqB):
    n = len(TseqA)
    pairs_table = [None]*n
    for i in range(n):
        pairs_table[i] = [i, TseqA[i][0], TseqB[i][0], 0, 1]
    return pairs_table
