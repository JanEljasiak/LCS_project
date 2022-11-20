# W tym pliku znajduje się nasza implementacja algorytmu FLCS wraz z potrzebnymi funkcjami

def build_successor_tables(seqA, seqB):
    seqAWithSpace, seqBWithSpace = " " + seqA, " " + seqB
    n1, n2 = len(seqAWithSpace), len(seqBWithSpace)
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

def pairs(T):
    TseqA, TseqB = T
    n = len(TseqA)
    pairsTable = [None]*n
    for i in range(n):
        pairsTable[i] = [i, TseqA[i][0], TseqB[i][0], 0, -1, 1]
                            # (k,i,j,level,pre,active)
    return pairsTable

def pairs_complete(T, pairsTable):
    TseqA, TseqB = T
    n = len(TseqA)
    while any(item[5] == 1 for item in pairsTable):
        for identicalPair in filter(lambda x: x[5] == 1, pairsTable):
            k = max(x[0] for x in pairsTable) + 1
            for i in range(n):
                el1 = TseqA[i][identicalPair[1]]
                el2 = TseqB[i][identicalPair[2]]
                if el1 != -1 and el2 != -1:
                    pairsTable.append([k + i, el1, el2, identicalPair[3] + 1, identicalPair[0], 1])
            pairsTable[pairsTable.index(identicalPair)][5] = 0
    return pairsTable