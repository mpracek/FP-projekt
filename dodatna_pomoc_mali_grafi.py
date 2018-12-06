# 115 120
def naredi_podgraf(mnozica):
    """"
    Iz danega grafa G dobimo mnozico vozlisc;
    iz te nato ta funkcija generira podgraf na danih vozliscih.
    """
    graf = dict()
    for element in mnozica:
        graf.update({element : G[element]})
    return graf


def potencna_mnozica(seznam):
    """
     Generator, ki vrne potencno mnozico.
    """
    if len(seznam) <= 1:
        yield seznam
        yield []
    else:
        for element in potenca_mnozica(seznam[1:]):
            yield [seznam[0]] + item
            yield element
##Popravi funkcijo izbrisi element!!!
def izbrisi_element_iz_vseh_gesel(slovar, element):
    """"
    Dan element izbrise iz vseh gesel slovarja.
    slovar = {1: ["a","b","c"], 2: ["a","e","f"], 3:["a","i"]}
    izbrisi_element_iz_vseh_gesel(slovar,"a"):
    >>slovar = {1: ["b","c"], 2: ["e","f"], 3:["i"]}
    """
    for kljuc in slovar:
        geslo = slovar[kljuc]
        seznam = list(geslo)
        for stevilo in range(len(seznam)):
            if seznam[stevilo] == element:
                del seznam[stevilo]
        geslo = geslo
        slovar.update({kljuc:geslo})
    return slovar