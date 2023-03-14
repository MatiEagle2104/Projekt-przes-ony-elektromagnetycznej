import math


# OBLICZENIA MATEMATYCZNE ZWIAZANE Z OSMIOKATEM FOREMNYM

def pole_osmiokata(a):
    p = 2 * (1 + math.sqrt(2)) * a * a
    return p


# wyciagniecie z dluzszej przekatnej (bedacej wymiarem liniowym) dlugosci boku
def dluzsza_przekatna_na_bok(d):
    a = d / (math.sqrt(4 + 2 * math.sqrt(2)))
    return a


# wysokosc osmiokata - odleglosc pomiedzy przeciwleglymi bokami
def wysokosc(a):
    r = a * (1 + math.sqrt(2))
    return r


# def odleglosc_po_przekatnej(a,odstep):
#     x = math.sqrt(2) * math.sqrt((2 * wysokosc(a) + odstep) * (2 * wysokosc(a) + odstep)) - wysokosc(a)
#     return x

def liczba_sasiadow(odstep, lam, a):
    sasiedzi = 0
    if odstep < (lam / 2):
        sasiedzi += 2
#    if odleglosc_po_przekatnej(a, odstep) < (lam / 2):
#        sasiedzi += 4
    return sasiedzi


def skutecznosc_ekranowania(l, lam, sasiedzi):
    if sasiedzi > 0:
        s = 20 * math.log10(lam / (2 * l)) - 20 * math.log10(math.sqrt(sasiedzi))
    else:
        s = 20 * math.log10(lam / (2 * l))
    return s


def max_wymiar_liniowy(lam, min_skutecznosc):
    x = 0.0001
    s = min_skutecznosc
    while s > min_skutecznosc or s == min_skutecznosc:
        x += 0.0001
        s = 20 * math.log10(lam / (2 * x))
    return x


def przeslona(lam, x, min_skutecznosc):
    wynik = ["", "", "", "", "", "", "", "", ""]
    wymiar_liniowy = 0.0001
    while wymiar_liniowy < max_wymiar_liniowy(lam, min_skutecznosc):
        wymiar_liniowy += 0.0001
        odstep = lam / 10
        while odstep < lam / 2:
            odstep += 0.0001 
            s = skutecznosc_ekranowania(wymiar_liniowy, lam,
                                        liczba_sasiadow(odstep, lam, dluzsza_przekatna_na_bok(wymiar_liniowy)))
            if s > min_skutecznosc or s == min_skutecznosc:
                ile_rz_w = math.floor((x - odstep) / (wymiar_liniowy + odstep))
                l_otworow = ile_rz_w * ile_rz_w
                wynik[0] = lam
                wynik[1] = s
                wynik[2] = odstep
                wynik[3] = ile_rz_w
                wynik[4] = l_otworow
                wynik[5] = dluzsza_przekatna_na_bok(wymiar_liniowy)
                wynik[6] = pole_osmiokata(wynik[5])
                wynik[7] = (wynik[6] * l_otworow) / (0.5 * 0.5)
                wynik[8] = (x - wynik[3] * wysokosc(dluzsza_przekatna_na_bok(wymiar_liniowy)) - (
                            wynik[3] - 1) * odstep) / 2
    return wynik


def wypisanie_wyniku(wyniki, f):
    print("PROJEKT PRZESLONY - WYNIKI:")
    print("---------------------------")
    print("czestotliwosc walidacyjna - f =", f / 1000000000, "[GHz]")
    print("lambda -", wyniki[0] * 1000, "[mm]")
    print("S = {:.4f}".format(wyniki[1]), "[dB]")
    print("Otwory -", wyniki[3], "x", wyniki[3])
    print("Laczna iczba otworow -", wyniki[4])
    print("Odleglosc otworow brzegowych od krawedzi - {:.2f}".format(wyniki[8] * 100), "[cm]")
    print("Odstepy pomiedzy otworami: {:.2f}".format(wyniki[2] * 100), "[cm]")
    print("Osmiokat ma bok o dlugosci {:.2f}".format(wyniki[5] * 100), "[cm]")
    print("Pole powierzchni jednego otworu - {:.2f}".format(wyniki[6] * 10000), "[cm^2]")
    print("Stosunek pola powierzchni otworow do pola przeslony - {:.2f}".format(wyniki[7] * 100), "%")
    return None


def main():
    f = 0.10 * 25 * math.pow(10, 9)
    v = 3 * math.pow(10, 8)
    lam = v / f
    x = 0.5
    min_skutecznosc = 15

    wygenerowana_przeslona = przeslona(lam, x, min_skutecznosc)
    wypisanie_wyniku(wygenerowana_przeslona, f)


main()
