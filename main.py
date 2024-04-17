fundusz = {
    "galeon" : 0,
    "sykl" : 0,
    "knut" : 13
}



def waluta_dict_na_str(fundusz):
    for k, v in fundusz.items():
        if k in fundusz and v != 0:
            fundusz[k] = v
    cena = ""

    if fundusz['galeon'] != 0:
        cena += str(fundusz['galeon']) + ' galeon '
    if fundusz['sykl'] != 0:
        cena += str(fundusz['sykl']) + ' sykl '
    if fundusz['knut'] != 0:
        cena += str(fundusz['knut']) + ' knut'

    return print(cena.strip())


waluta_dict_na_str(fundusz)


