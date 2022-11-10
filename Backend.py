# W tym pliku znajduje się nasza implementacja algorytmu FLCS wraz z potrzebymi funkcjami

def funkcja():
    Chcesz_sie_bawic = True
    while Chcesz_sie_bawic:

        licznik = int(input("Podaj liczbę od 1 do 5 (poza 4)"))
        if licznik not in [1, 2, 3, 5]:
            print("Bardzo nieładne zachowanie ;/ ")
            Chcesz_sie_bawic = False
        if licznik == 1:
            print("Janek pozdrawia prowadzacego!")
        if licznik == 2:
            print("Damian pozdrawia prowadzacego!")
        if licznik == 3:
            print("Karol pozdrawia prowadzacego!")
        if licznik == 5:
            print("Wszyscy pozdrawiamy prowadzacego!")
        Chcesz_sie_bawic = bool(input("Czy dalej chcesz sie bawić? (Tak- wpisz cokolwiek/dosyć tego- zostaw puste pole)"))
        print("Miłego dnia")


funkcja()


