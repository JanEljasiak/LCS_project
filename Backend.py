# W tym pliku znajduje się nasza implementacja algorytmu FLCS wraz z potrzebnymi funkcjami

def build_successor_tables(seqA, seqB):
    seqAWithSpace, seqBWithSpace = " " + seqA, " " + seqB
    colDim1, colDim2 = len(seqAWithSpace), len(seqBWithSpace)
    distinctLetters = "".join(dict.fromkeys(seqA + seqB))
    rowDim = len(distinctLetters)
    TseqA = [[-1 for col in range(colDim1)] for row in range(rowDim)]
    TseqB = [[-1 for col in range(colDim2)] for row in range(rowDim)]
    for i in range(rowDim):
        for j in range(colDim1):
            TseqA[i][j] = seqAWithSpace.find(distinctLetters[i], j+1)
        for j in range(colDim2):
            TseqB[i][j] = seqBWithSpace.find(distinctLetters[i], j+1)
    return TseqA, TseqB, rowDim

def pairs(matricesWithRowDim):
    TseqA, TseqB, rowDim = matricesWithRowDim
    pairsTable = [None]*rowDim
    for i in range(rowDim):
        pairsTable[i] = [i, TseqA[i][0], TseqB[i][0], 0, -1, 1]
                            # (k,i,j,level,pre,active)
    return pairsTable

def pairs_complete(matricesWithRowDim, pairsTable):
    TseqA, TseqB, rowDim = matricesWithRowDim
    while any(item[5] == 1 for item in pairsTable):
        for identicalPair in filter(lambda x: x[5] == 1, pairsTable):
            maximalRow = max(x[0] for x in pairsTable) + 1
            for i in range(rowDim):
                el1 = TseqA[i][identicalPair[1]]
                el2 = TseqB[i][identicalPair[2]]
                if el1 != -1 and el2 != -1:
                    pairsTable.append([maximalRow + i, el1, el2, identicalPair[3] + 1, identicalPair[0], 1])
            pairsTable[pairsTable.index(identicalPair)][5] = 0
    return pairsTable

def function(pairsTable, seqA):
    seqAWithSpace = " " + seqA
    maximalLevel = max(x[0] for x in pairsTable)
    identicalPairsWithMaximalLevel = filter(lambda x: x[3] == maximalLevel, pairsTable)
    numberOfLCS = len(identicalPairsWithMaximalLevel)
    LCS = [None] * numberOfLCS
    for identicalPair in identicalPairsWithMaximalLevel:
        i = 0
        tempPair = identicalPair
        LCSs = seqAWithSpace[tempPair[1]]
        for j in range(maximalLevel-1):
            tempPair = filter(lambda x: x[0] == tempPair[4], pairsTable)
            LCSs = seqAWithSpace[tempPair[1]] + LCSs
        LCS[i] = LCSs
        i += 1
    return LCS

a = build_successor_tables("CAGTT", "AGTAC")
print(function(pairs_complete(a, pairs(a)), "CAGTT"))