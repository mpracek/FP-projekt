# 115 120
"""
V tej datoteki se nahaja program, ki nam bo generiral majhne grafe.
"""

def generator(stevilo_vozlisc):
    """
    Funkcija bo vrnila vse grafe velikosti stevilo_vozlisc v obliki seznama slovarja seznama sosedov.
    generator(1)
    >> {1:None}
    genretor(2)
    >>[{1: 2, 2:1}, {1:None, 2:None}]
    """
