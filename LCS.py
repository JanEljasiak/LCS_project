# LCS - podstawowa wersja algorytmu

def LCS(seqA, seqB):
    m = len(seqA) + 1
    n = len(seqB) + 1
    M = [[0 for col in range(n)] for row in range(m)] #tworzymy macierz zer
    for i in range(1, m): #uzupełniamy macierz zgodnie z algorytmem
        for j in range(1, n):
            if seqA[i-1] == seqB[j-1]:
                M[i][j] = M[i-1][j-1] + 1
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])
    #przechodzimy po wybranych elementach macierzy, tworząc LCS
    i = m-1
    j = n-1
    res = [""]*M[i][j]
    while i > 0 and j > 0:
        if seqA[i-1] == seqB[j-1]:
            res[M[i][j]-1] = seqA[i-1]
            i -= 1
            j -= 1
        elif M[i-1][j] > M[i][j-1]:
            i -= 1
        else:
            j -= 1
    print(res)

LCS("GCCCTAGCG", "GCGCAATG")