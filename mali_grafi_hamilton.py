# 115 120
import dodatna_pomoc_mali_grafi
import mali_grafi_neenakost

def neenakost(G):
    """"
    Funkcija nam pove, ali graf ustreza neeenakosti, ki jo zahteva konjektura.
    """
    if neodvistnost(G) <= 1 + povprecna_lokalna(G):
        return True
    else:
        return False

def hamiltonska_pot(G,zacetno_vozlisce):
    """"
    G je prej generiran graf, za katerega smo potrdili neenakost.
    Zacetno vozlisce je vozlisce, ki smo ga dolocili, da zacne nase zaporedje;
    sicer ni pomembno za pot, ki mora obiskati vsa vozlisca, a potrebujemo zacetek.

    Ce graf neenakosti ne zadosca, nam funkcija vrne Ta graf nas ne zanima,
    drugace se izvede program.
    """
    zaporedje = [zacetno_vozlisce]
    #izbrisi_element_iz_vseh_gesel(G, zacetno_vozlisce)
    seznam = G[zacetno_vozlisce]
    for sosed in seznam:
        zaporedje.append(sosed)
        izbrisi_element_iz_vseh_gesel(G, sosed)


