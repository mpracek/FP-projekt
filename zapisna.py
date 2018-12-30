#115 120
#V tej datoteki bo zapisan celoten genetski algoritem, ki bo izvedel naš program. Zapisan je v jeziku Sage.
#Želimo dokazati, da obstaja graf G, za katerega ne velja, da zadošča neenakosti 
#neodvistnostno število(G) =< 1 + povprečna lokalna neodvistnost(G)
#in nima Hamiltonove poti.

def nasi_grafi(stevilo_vozlisc):
    """
    Funkcija, ki nam vrne enostavne povezane grafe na dolocenem stevilu vozlisc.
    """
    grafi = list(graphs.nauty_geng(str(stevilo_vozlisc)+" -c"))
    return grafi

def neodvistnostno_stevilo(G):
    """
    Vrne neodvistno število grafa G
    Za pomoč uporabimo independet_set() iz modula neusmerjenih grafov.
    """
    neodvisno = G.independent_set()
    dolzina = len(neodvisno)
    return dolzina
    
    
def naredi_podgraf(G, seznam):
    """
    Funkcija, ki nam za dan seznam vozlišč vrne podgraf, definiran na le teh
    Seznam je tukaj nabor vozlišč, ki nas zanimajo.
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

def preverjanje_za_en_graf(G):
    """
    Preveri, ali za en graf velja, če je ta graf izjema.
    """
    if neodvisnostno_stevilo(G) <= 1 + povprecna(G):
            if hamiltonian.path(G) == None:
                graf = str(G)
                return "Ovrgli smo domnevo in izjema je" + graf
    else:
        return "Izjeme nismo ovrgli"

def preverjanje(stevilo_vozlisc):
    """
    Preveri veljavnost konjekture za vse grafe na določenem številu vozlišč.
    """
    for G in nasi_grafi(stevilo_vozlisc):
       if neodvisnostno_stevilo(G) <= 1 + povprecna(G):
            if hamiltonian.path(G) == None:
                graf = str(G)
                return "Ovrgli smo domnevo in izjema je" + graf
    else:
        return "Izjeme nismo ovrgli"

##Genetski algoritem 
import random
import operator
import math

##Initalization -> izbira števila začetnega vzorca
def poisson(t = 1, lambd = 1/2):
    """
    S to funkcijo določimo začetno število vozlišč
    """
    stevilo_vozlisc = 0
    racunalo = 0
    while racunalo < t:
        stevilo_vozlisc += 1
        racunalo += random.expovariate(lambd)
    return stevilo_vozlisc
		
#Zanimajo nas zgolj enostavni, povezani grafi, zato bomo definirali začetno množico.
def zacetna_populacija():
    """
    Ta funkcija nam da grafe, na katerih bo opravljen prvi test.
    """	
    stevilo_vozlisc = poisson(t = 1, lambd = 1/2)
    return nasi_grafi(stevilo_vozlisc)
    
#V tem koraku moramo določiti primerno začetno množico grafov
# Določiti moramo primeren kriterij,
#po katerem bomo grafe iz naše začetne množice razporedili

#Odločimo se za čim manjša razlika med neodvisnostnim številom in povprečno lokalno neodvisnostjo
def kriterij():
    """"
    Izračuna kriterij, po katerem vse elemente razporedimo.
    """
    populacija = zacetna_populacija()
    slovar = dict()
    for element in populacija:
        racun = neodvisnostno_stevilo(element)- povprecna(element)
        slovar[element] = racun
    return slovar

def razporedi():
    """
    Razporedi elemente začetne populacije.
    """
    populacija = kriterij()
    ###POVPRAŠAJ ZA ITEMGETTER
    razporejena_populacija = sorted(slovar.items(), key = operator.itemgetter(1))
    nasa_populacija = []
    for osebek in razporejena_populacija:
        nasa_populacija.append(populacija[osebek[0]])
    return nasa_populacija
    
def zacetna_testna_populacija():
    """
    Za začetni parameter izberemo zacetna_populacija(), ki nam bo vrnila
    vse grafe začetne velikosti.
    Najprej moramo določiti, kolikšen del začetne populacije bomo testirali
    V genetiki velja, da ostanejo zgolj najbojši, zato bomo vzeli le najboljše,
    torej tiste, pri katerih bo kriterij največji.
    """
    populacija = zacetna_populacija()
    delez = random.uniform(0,1)
    odstotek = math.floor( 100 * delez)/100
    dolzina = len(zacetna_populacija())

    vrednost = math.floor(odsotek * dolzina)
    testna_populacija = populacija[:vrednost]
    return testna_populacija

def zacetni_test()
    """
    Funkcija izvede test za našo začetno testno populacijo.
    """
    zanima_nas = zacetna_testna_populacija()
    for graf in zanima_nas:
        preverjanje_za_en_graf(graf)

        
#Ko smo opravili začetni test sledi priprava nove generacije,
#kjer nove testne primerke pripravimo skozi rekombinacijo in mutacijo.

def mutacija_povezava():
    """
    Spremeni graf tako, da mu doda povezavo
    """
     zacetna = zacetna_testna_populacija()
	naslednja_povezave = []
	for graf in zacetna:
    		vozlisca = list(graf.keys())
    		vozlisce1 = random.choice(vozlisca)
    		#v nabor spadajo vsa vozli��a, ki niso niti vozlisce1, niti njegovi sosedi.


### uredi ta nabor!!!!!!
		nabor = 
    		nabor = list(nabor)
		vozlisce2 = random.choice(nabor)
		graf.add_edge(vozlisce1, vozlisce2)
		naslednja_povezave.append(graf)
	return naslednja_povezave

def mutacija_vozlisce():
"""
Doda vozlisce in mu nato doda nekaj povezav nanj.
"""	
	zacetna = zacetna_testna_populacija()
	naslednja_vozlisce = []
	dolzina = len(zacetna)
	for graf in zacetna:
		graf.add_vertex(novo)
		stevilo = randint(0,dolzina)
		vozlisca = list(graf.keys())
		dodaj_vozlisca = random.sample(vozlisca, stevilo)
		for i in range(stevilo):
			graf.add_edge(novo, dodaj_vozlisca[i])
		naslednja_vozlisce.append(graf)
	return naslednje_vozlisce	
	
def crossover()
		