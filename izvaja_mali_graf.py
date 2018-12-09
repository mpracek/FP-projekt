"""
Tukaj bomo imeli program, ki se bo skliceval na ostale funkcije, ki smo jih prej definirali.
"""
import dodatna_pomoc_mali_grafi
import mali_grafi_generator
import mali_grafi_hamilton
import mali_grafi_neenakost

def pregled_malih_grafov(n):
    """
    S funkcijo pregled_malih_grafov bomo pregledali vse grafe na <= n vozliscih.
    Ce bomo nasli protiprimer, da bomo dodali v seznam protiprimerov
    """
    protiprimer = []
    for