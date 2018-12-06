#  115 120
import dodatna_pomoc_mali_grafi

""""
Graf G mora biti prikazan s seznamom sosedov. G generiramo prej.
"""
def neodvisnost(G):
    """"
    Vrne neodvistnostno stevilo grafa G.
    """
    moc = 0
    vsa_vozlisca = G.keys()
    potencna = potencna_mnozica(vsa_vozlisca)
    for element in potencna:
        for vozlisce in element:
            for naslednji in element:
                if naslednji in G[element]:
                    moc = moc
        moc = len(element)
    return moc

def lokalna(G, vozlisce):
    """"
    Vrne lokalno neodvistnost grafa G za vozlisce.
    """
    mnozica = G[vozlisce]
    novGraf = naredi_podgraf(mnozica)
    lokalna_neodvistnost = neodvisnost(novGraf)
    return lokalna_neodvistnost

def povprecna_lokalna(G):
    """"
    Vrne povprecno lokalno neodvistnost.
    """
    vsota = 0
    stevilo_vozlisc = 0
    lokalna_kljuc = 0

    for kljuc in G:
        lokalna_kljuc = lokalna(G, kljuc)
        vsota += lokalna_kljuc
        stevilo_vozlisc += 1
    povprecje = vsota/stevilo_vozlisc
    return povprecje


