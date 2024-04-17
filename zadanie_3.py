def licz_sume(dane):

    przelicznik = {
        "sykl": {"na_galeon": 1 / 17},
        "knut": {"na_galeon": 1 / (17 * 21), "na_sykl": 1 / 21}
    }

    wynik = {
        "galeon": 0,
        "sykl": 0,
        "knut": 0
    }

    for klucz, wartosci in dane.items():
        for i, wartosc in enumerate(wartosci):
            if klucz == "galeon":
                wynik["galeon"] += wartosc
            elif klucz == "sykl":
                wynik["sykl"] += wartosc
            elif klucz == "knut":
                wynik["knut"] += wartosc

    wynik["knut"] = 0
    wynik["sykl"] += wynik["knut"] *21
    wynik["galeon"] += wynik["knut"] // (17 * 21)
    wynik["knut"] %= 17 * 21

    return wynik

# dane = {
#         "galeon": [1, 3, 5],
#         "sykl": [18, 20, 10],
#         "knut": [30, 40, 7]
#     }

galeon = list(map(int, input("Podaj ilość monet galeon (oddzielone przecinkami): ").split(',')))
sykl = list(map(int, input("Podaj ilość monet sykl (oddzielone przecinkami): ").split(',')))
knut = list(map(int, input("Podaj ilość monet knut (oddzielone przecinkami): ").split(',')))

dane = {
    "galeon": galeon,
    "sykl": sykl,
    "knut": knut
}

print(licz_sume(dane))



