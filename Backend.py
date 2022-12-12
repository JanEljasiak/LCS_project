# W tym pliku znajduje się nasza implementacja algorytmu FLCS wraz z potrzebnymi funkcjami

def validate(seq):
    for letter in seq:
        if letter not in ["A", "C", "G", "T"]:
            raise ValueError("Sekwencje muszą być ciągiem liter należących do ustalonego alfabetu.")
    if not seq:
        raise ValueError("Żadna z podanych sekwencji nie może być pusta.")

def build_successor_tables(seqA, seqB):
    seqAWithSpace, seqBWithSpace = " " + seqA, " " + seqB
    colDimA, colDimB = len(seqAWithSpace), len(seqBWithSpace)
    distinctLetters = "".join(dict.fromkeys(seqA + seqB))
    rowDim = len(distinctLetters)
    TseqA = [[-1 for col in range(colDimA)] for row in range(rowDim)]
    TseqB = [[-1 for col in range(colDimB)] for row in range(rowDim)]
    for i in range(rowDim):
        for j in range(colDimA):
            TseqA[i][j] = seqAWithSpace.find(distinctLetters[i], j+1)
        for j in range(colDimB):
            TseqB[i][j] = seqBWithSpace.find(distinctLetters[i], j+1)
    return TseqA, TseqB, rowDim

def pairs(matricesWithRowDim):
    TseqA, TseqB, rowDim = matricesWithRowDim
    pairsTable = list()
    for i in range(rowDim):
        if TseqA[i][0] != -1 and TseqB[i][0] != - 1:
            pairsTable.append([i, TseqA[i][0], TseqB[i][0], 0, -1, 1])
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

def find_list_of_LCS(pairsTable, seqA):
    seqAWithSpace = " " + seqA
    maximalLevel = max(x[3] for x in pairsTable)
    identicalPairsWithMaximalLevel = list(filter(lambda x: x[3] == maximalLevel, pairsTable))
    numberOfLCS = len(identicalPairsWithMaximalLevel)
    listOfLCS = [None] * numberOfLCS
    for i, identicalPair in enumerate(identicalPairsWithMaximalLevel):
        tempPair = identicalPair
        LCS = seqAWithSpace[tempPair[1]]
        for j in range(maximalLevel):
            tempPair = list(filter(lambda x: x[0] == tempPair[4], pairsTable))[0]
            LCS = seqAWithSpace[tempPair[1]] + LCS
        listOfLCS[i] = LCS
    return listOfLCS

def LCS(seqA, seqB):
    validate(seqA)
    validate(seqB)
    matricesWithRowDim = build_successor_tables(seqA, seqB)
    pairsTable = pairs_complete(matricesWithRowDim, pairs(matricesWithRowDim))
    return find_list_of_LCS(pairsTable, seqA)