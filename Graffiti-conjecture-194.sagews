︠dc478ac5-b734-48af-b21e-2f5add0914ab︠

︡40044475-9905-452d-bda6-0feb025b13a0︡
︠8c42cd13-bb71-41e7-8eba-c2e2d21f9388s︠
#115 120
#V tej datoteki bo zapisan celoten genetski algoritem, ki bo izvedel nas program. Zapisan je v jeziku Sage.
#Zelimo dokazati, da obstaja graf G, za katerega ne velja, da zadosca neenakosti
# neodvistnostno število(G) =< 1 + povprecna lokalna neodvistnost(G) in nima Hamiltonove poti.

import random
import operator
import math

def nasi_grafi(stevilo_vozlisc):
    """
    Funkcija, ki nam vrne enostavne povezane grafe na dolocenem stevilu vozlisc.
    """
    grafi = list(graphs.nauty_geng(str(stevilo_vozlisc)+" -c"))
    return grafi

def neodvistnostno_stevilo(G):
    """
    Vrne neodvistno število grafa G
    Za pomoc uporabimo independet_set() iz modula neusmerjenih grafov.
    """
    neodvisno = G.independent_set()
    dolzina = len(neodvisno)
    return dolzina


def naredi_podgraf(G, seznam):
    """
    Funkcija, ki nam za dan seznam vozlisc vrne podgraf, definiran na le teh
    Seznam je tukaj nabor vozlisc, ki nas zanimajo.
    """
    nov_graf = dict()
    for vozlisce in G:
        if vozlisce not in seznam:
            G.pop(vozlisce)
        else:
            for sosed in G[vozlisce]:
                sosedi = G[vozlisce]
                if sosed not in seznam:
                    sosedi.remove(sosed)
            nov_graf[sosed] = sosedi
    return nov_graf


def lokalna_neodvistnost(G, vozlisce):
    """
    Vrne lokalno neodvistnost grafa G v vozliscu v.
    Lokalna neodvistnost je neodvistnost podgrafa, ki ga določajo sosedi vozlišča v,
    za nek v iz množice vozlišč.
    """
    mnozica = G[vozlisce]
    novGraf = naredi_podgraf(G, mnozica)
    lokalna_neodvistnost = neodvisnost(novGraf)
    return lokalna

def povprecna(G):
    """
    Vrne povprečno lokalno neodvisnost grafa G
    """
    povprecje =  0
    for vozlisce in G:
        povprecje += lokalna_neodvisnost(G, vozlisce)
    povprecna_vrednost  = povprecje/ len(G)
    return povprecna_vrednost

def preverjanje_za_en_graf(G, maksimalna):
    """
    Preveri, ali za en graf velja, če je ta graf izjema.
    """
    if neodvisnostno_stevilo(G) <= 1 + povprecna(G):
            if hamiltonian.path(G) == None:
                graf = str(G)
                return "Ovrgli smo domnevo in izjema je" + 	graf
    else:
        return "Izjeme nismo ovrgli"

def preverjanje(stevilo_vozlisc, maksimalna):
    """
    Preveri veljavnost konjekture za vse grafe na določenem številu vozlišč.
    """
    for G in nasi_grafi(stevilo_vozlisc):
        if neodvisnostno_stevilo(G) <= 1 + povprecna(G):
            if hamiltonian.path(G) == None:
                graf = str(G)
                return "Ovrgli smo domnevo in izjema je" + 	graf
    return "Izjeme nismo ovrgli"

##Genetski algoritem

##Initalization -> izbira stevila zacetnega vzorca
def poisson(t = 1, lambd = 1/2):
    """
    S to funkcijo določimo začetno stevilo vozlisc
    """
    stevilo_vozlisc = 0
    racunalo = 0
    while racunalo < t:
        stevilo_vozlisc += 1
        racunalo += random.expovariate(lambd)
    return stevilo_vozlisc

#Zanimajo nas zgolj enostavni, povezani grafi, zato bomo definirali zacetno mnozico.
def zacetna_populacija(maksimalna):
    """
    Ta funkcija nam da grafe, na katerih bo opravljen prvi test.
    Maksimalna nam pove, koliko je največja (maksimalna) velikost vsake generacije.
    """
    stevilo_vozlisc = poisson(t = 5, lambd = 1/2)
    populacija = []
    stevec = 0
    while stevec < maksimalna:
        graf = graphs.RandomGNP(stevilo_vozlisc, random.uniform(0, 1))
        if graf.is_connected():
            populacija.append(graf)
            i += 1
    return populacija

#V tem koraku moramo dolocti primerno začetno mnozico grafov
# Dolociti moramo primeren kriterij,po katerem bomo grafe iz nase zacetne mnozice razporedili
#Odlocimo se za cim manjse neodvisnostno stevilo

def razporedi(populacija = zacetna_populacija(maksimalna)):
    """
    Izracuna kriterij, po katerem vse elemente razporedimo in razporedi elemente populacije.
    """
    slovar = dict()
    for element in populacija:
        slovar[element] = neodvistnostno_stevilo(element)
    razporejena_populacija = sorted(slovar.items(), key = operator.itemgetter(1))
    nasa_populacija = []
    for osebek in razporejena_populacija:
        nasa_populacija.append(populacija[osebek[0]])
    return nasa_populacija

def testna_populacija(maksimalna):
    """
    Za zacetni parameter izberemo zacetna_populacija(), ki nam bo vrnila
    vse grafe zacetne velikosti.
    Najprej moramo določiti, kolikšen del začetne populacije bomo testirali
    V genetiki velja, da ostanejo zgolj najboljsi, zato bomo vzeli le najboljse,
    torej tiste, z minimalnim neodvistnostnim številom.
    """
    populacija = razporedi()
    if len(populacija) > maksimalna:
        testna_populacija = populacija[:vrednost]
    else:
        testna_populacija = populacija
    return testna_populacija


#Ko smo opravili zacetni test sledi priprava nove generacije,
#kjer nove testne primerke pripravimo skozi rekombinacijo in mutacijo.

def doda_povezavo(graf):
    """
    Spremeni graf tako, da mu doda povezavo
    """
    vozlisca = graf.keys()
    vozlisce1 = random.choice(vozlisca)
    vozlisce2 = random.choice(vozlisca)
    if vozlisce1 != vozlisce2:
        graf.add_edge(vozlisce1, vozlisce2)
    return graf


def odstrani_povezavo(graf):
    """
    Odstrani nakljucno povezavo iz grafa;
    Pazimo, da mora graf, ki ga dobimo, biti povezan.
    """
    kopija = Graph(graf, immutable=True)
    vozlisce1 = kopija.random_vertex()
    vozlisce2 = kopija.random_vertex()
    if vozlisce1 != vozlisce2:
        kopija.delete_edge(vozlisce1, vozlisce2)
        if kopija.is_connected():
            return kopija
        else:
            kopija.add_edge(vozlisce1, vozlisce2)


def mutacija_vozlisce(graf):
    """
    Doda vozlisce in mu nato doda nekaj povezav nanj.
    """
    dolzina = len(graf.keys())
    graf.add_vertex(novo)
    stevilo = randint(0,dolzina)
    vozlisca = list(graf.keys())
    dodaj_vozlisca = random.sample(vozlisca, stevilo)
    for i in range(stevilo):
        graf.add_edge(novo, dodaj_vozlisca[i])
    return graf

def odstrani_vozlisce(graf):
    vozlisca = list(graf.keys())
    vozlisce1 = random.choice(vozlisca)
    graf.delete_vertex(vozlisce1)
    if graf.is_connected():
        return graf

def mutacija(graf):
    """
    Na grafu lahko odstranimo, dodamo povezavo, dodamo, odstranimo vozlisce in vsako kombinacijo le teh.
    """
    p = random.uniform(0,1)
    if p <= 1/15:
        odstrani_vozlisce(graf)
    elif p > 1/15 and p <= 2/15:
         mutacija_vozlisce(graf)
    elif p > 2/15 and p <= 3/15:
        odstrani_povezavo(graf)
    elif p > 3/15 and p <= 4/15:
        doda_povezavo(graf)
    elif p > 4/15 and p <= 5/15:
        sprememba = odstrani_vozlisce(graf)
        mutacija_vozlisce(sprememba)
    elif p > 5/15 and p <= 6/15:
        sprememba = odstrani_vozlisce(graf)
        odstrani_povezavo(sprememba)
    elif p > 6/15 and p <= 7/15:
        sprememba = odstrani_vozlisce(graf)
        doda_povezavo(sprememba)
    elif p > 7/15 and p <= 8/15:
        sprememba = mutacija_vozlisce(graf)
        odstrani_povezavo(sprememba)
    elif p > 8/15 and p <= 9/15:
        sprememba = mutacija_vozlisce(graf)
        doda_povezavo(sprememba)
    elif p > 9/15 and p <= 10/15:
        sprememba = odstrani_povezavo(graf)
        doda_povezavo(sprememba)
    elif p > 10/15 and p <= 11/15:
        sprememba = mutacija_vozlisce(graf)
        sprememba2 = doda_povezavo(sprememba)
        odstrani_povezavo(sprememba2)
    elif p > 11/15 and p <= 12/15:
        sprememba = mutacija_vozlisce(graf)
        sprememba2 = doda_povezavo(sprememba)
        odstrani_povezavo(sprememba2)
    elif p > 12/15 and p <= 13/15:
        sprememba = mutacija_vozlisce(graf)
        sprememba2 = odstrani_vozlisce(sprememba)
        odstrani_povezavo(sprememba2)
    elif p > 13/15 and p <= 14/15:
        sprememba = mutacija_vozlisce(graf)
        sprememba2 = doda_povezavo(sprememba)
        odstrani_vozlisce(sprememba2)
    elif p > 14/15 and p <= 15/15:
        sprememba = mutacija_vozlisce(graf)
        sprememba2 = doda_povezavo(sprememba)
        sprememba3 = odstrani_povezavo(sprememba2)
        odstrani_vozlisce(sprememba3)

def nova_populacija(populacija = testna_populacija(maksimalna), verjetnost = 0.05):
    """
    Vsak graf iz populacije z neko verjetnostjo spremenimo.
    Za zacetku za populacijo uporabimo zacetna_testna_populacija()
    Ti spremenjeni grafi nam dajo novo populacijo.
    """
    naslednja_generacija = []
    for i in range(len(populacija)):
        q = random.uniform(0,1)
        r = random.uniform(0,1)
        prob = q * r
        if verjetnost < prob:
            naslednja_generacija[i] = mutacija(populacija[i])
        else:
            naslednja_generacija[i] = populacija[i]
    return naslednja_generacija

# osebka imata samo enega potomca
# n = stevilo vozlisc
def crossover(n, osebek1, osebek2):
    """
    V nasem primeru je n stevilo vozlisc.
    """
    while True:
        subgraf1 = osebek1.random_subgraph(0.5)
        subgraf2 = osebek2.random_subgraph(0.5)
        if len(subgraf1.vertices()) + len(subgraf2.vertices()) == n and len(subgraf1.vertices()) >= 1 and len(subgraf1.vertices()) < n and subgraf1.is_connected() and subgraf2.is_connected():
            subgraf1.relabel()
            subgraf2.relabel()
            potomec = subgraf1.disjoint_union(subgraf2)
            # lambda se spreminja z stevilom vozlisc
            nove_povezave = poisson(lambd = log(n/2))
            for k in range(nove_povezave):
                a = subgraf1.random_vertex()
                b = subgraf2.random_vertex()
                potomec.add_edge((0, a), (1, b))
            potomec.relabel()
            break
    return potomec

def potomci(populacija = nova_populacija(populacija = testna_populacija(maksimalna), verjetnost = 0.05)):
    nova_populacija = populacija
    stevilo_parjenj = poisson(t = len(populacija))
    for k in range(stevilo_parjenj):
        starsa = random.sample(populacija, k = 2)
        nova_populacija.append(crossover(n, starsa[0], starsa[1]))
    return nova_populacija


def KoncniTestGA(konec,maksimalna):
    """
    Konec pove, koliko generacij naj pogledamo.
    """
    populacija = testna_populacija(maksimalna)
    i = 1
    while i <= konec:
        populacija = potomci(populacija)
        populacija = mutacija(populacija)
        populacija = testna_populacija(populacija)
        for i in range(len(populacija)):
            G = populacija[i]
            if neodvistnostno_stevilo(G) <= 1 + povprecna(G):
                if hamiltonian.path(G) == None:
                    print (G)
                    return "Ovrgli smo domnevo"

                i += 1
    return "Domneva ni ovrzena."
︡5385e434-f8a6-4e31-b93b-40fa3427ec07︡{"stderr":"\n\n*** WARNING: Code contains non-ascii characters    ***\n\n\nError in lines 74-83\nTraceback (most recent call last):\n  File \"/cocalc/lib/python2.7/site-packages/smc_sagews/sage_server.py\", line 1188, in execute\n    flags=compile_flags) in namespace, locals\n  File \"\", line 1, in <module>\nNameError: name 'maksimalna' is not defined\n"}︡{"done":true}︡
︠d5abe42a-f839-43bb-8503-c3dad2ed788f︠


















