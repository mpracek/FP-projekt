# 115 120
"""
V tej datoteki se nahaja program, ki nam bo generiral majhne grafe.
"""
import dodatna_pomoc_mali_grafi

def generator(stevilo_vozlisc):
    """
    Funkcija bo vrnila vse grafe velikosti stevilo_vozlisc v obliki seznama slovarja seznama sosedov.
    generator(1)
    >> {1:None}
    generator(2)
    >>[{1: 2, 2:1}, {1:None, 2:None}]
    """
    vsi_grafi = []
    graf = dict()
    seznam_vozlisc = [None]
    for stevilo in stevilo_vozlisc:
        graf.update({stevilo: None})
        seznam_vozlisc.append(stevilo)
    obogaten_seznam = potencna_mnozica(seznam_vozlisc)






