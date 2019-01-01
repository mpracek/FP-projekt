#115 120
#V tej datoteki bo zapisan celoten genetski algoritem, ki bo izvedel naš program. Zapisan je v jeziku Sage.
#Želimo dokazati, da obstaja graf G, za katerega ne velja, da zadošèa neenakosti 
#neodvistnostno število(G) =< 1 + povpreèna lokalna neodvistnost(G)
#in nima Hamiltonove poti.

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
    Za pomoè uporabimo independet_set() iz modula neusmerjenih grafov.
    """
    neodvisno = G.independent_set()
    dolzina = len(neodvisno)
    return dolzina
    
    
def naredi_podgraf(G, seznam):
    """
    Funkcija, ki nam za dan seznam vozlišè vrne podgraf, definiran na le teh
    Seznam je tukaj nabor vozlišè, ki nas zanimajo.
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
    Lokalna neodvistnost je neodvistnost podgrafa, ki ga doloèajo sosedi vozlišèa v,
    za nek v iz množice vozlišè.
    """
    mnozica = G[vozlisce]
    novGraf = naredi_podgraf(G, mnozica)
    lokalna_neodvistnost = neodvisnost(novGraf)
    return lokalna

def povprecna(G):
    """
    Vrne povpreèno lokalno neodvisnost grafa G
    """
    povprecje =  0
    for vozlisce in G:
        povprecje += lokalna_neodvisnost(G, vozlisce)
    povprecna_vrednost  = povprecje/ len(G) 
    return povprecna_vrednost

def preverjanje_za_en_graf(G):
    """
    Preveri, ali za en graf velja, èe je ta graf izjema.
    """
    if neodvisnostno_stevilo(G) <= 1 + povprecna(G):
            if hamiltonian.path(G) == None:
                graf = str(G)
                return "Ovrgli smo domnevo in izjema je" + 	graf
    else:
        return "Izjeme nismo ovrgli"

def preverjanje(stevilo_vozlisc):
    """
    Preveri veljavnost konjekture za vse grafe na doloèenem številu vozlišè.
    """
    for G in nasi_grafi(stevilo_vozlisc):
       if neodvisnostno_stevilo(G) <= 1 + povprecna(G):
            if hamiltonian.path(G) == None:
                graf = str(G)
                return "Ovrgli smo domnevo in izjema je" + 	graf
    else:
        return "Izjeme nismo ovrgli"

##Genetski algoritem 

##Initalization -> izbira števila zaèetnega vzorca
def poisson(t = 1, lambd = 1/2):
    """
    S to funkcijo doloèimo zaèetno število vozlišè
    """
    stevilo_vozlisc = 0
    racunalo = 0
    while racunalo < t:
        stevilo_vozlisc += 1
        racunalo += random.expovariate(lambd)
    return stevilo_vozlisc
		
#Zanimajo nas zgolj enostavni, povezani grafi, zato bomo definirali zaèetno množico.
def zacetna_populacija():
    """
    Ta funkcija nam da grafe, na katerih bo opravljen prvi test.
    """	
    stevilo_vozlisc = poisson(t = 1, lambd = 1/2)
    return nasi_grafi(stevilo_vozlisc)
    
#V tem koraku moramo doloèiti primerno zaèetno množico grafov
# Doloèiti moramo primeren kriterij,
#po katerem bomo grafe iz naše zaèetne množice razporedili

#Odloèimo se za èim manjše neodvisnostno število

def kriterij(populacija):
    """"
    Izraèuna kriterij, po katerem vse elemente razporedimo.
    """
    slovar = dict()
    for element in populacija:
        racun = neodvisnostno_stevilo(element)
        slovar[element] = racun
    return slovar

def razporedi():
    """
    Razporedi elemente populacije.
    """
    populacija = kriterij()
    razporejena_populacija = sorted(slovar.items(), key = operator.itemgetter(1))
    nasa_populacija = []
    for osebek in razporejena_populacija:
        nasa_populacija.append(populacija[osebek[0]])
    return nasa_populacija
    
def testna_populacija():
    """
    Za zaèetni parameter izberemo zacetna_populacija(), ki nam bo vrnila
    vse grafe zaèetne velikosti.
    Najprej moramo doloèiti, kolikšen del zaèetne populacije bomo testirali
    V genetiki velja, da ostanejo zgolj najboljši, zato bomo vzeli le najboljše,
    torej tiste, z minimalnim neodvistnostnim številom.
    """
    populacija = razporedi()
    delez = random.uniform(0,1)
    odstotek = math.floor( 100 * delez)/100
    dolzina = len(zacetna_populacija())

    vrednost = math.floor(odsotek * dolzina)
    testna_populacija = populacija[:vrednost]
    return testna_populacija

def zacetni_test()
    """
    Funkcija izvede test za našo zaèetno testno populacijo.
    """
    zanima_nas = zacetna_testna_populacija()
    for graf in zanima_nas:
        preverjanje_za_en_graf(graf)

        
#Ko smo opravili zaèetni test sledi priprava nove generacije,
#kjer nove testne primerke pripravimo skozi rekombinacijo in mutacijo.

def doda_povezavo(graf):
    """
    Spremeni graf tako, da mu doda povezavo
    """
     	vozlisca = list(graf.keys())
    	vozlisce1 = random.choice(vozlisca)
    	seznam_vseh_vozlisc = list(graf.keys())
	seznam_sosedov =  graf[vozlisce1]
	for element in seznam_vseh_vozlisc:
		if element in seznam_sosedov:
			seznam_sosedov.remove(element)
	nabor = seznam_sosedov
    	nabor = list(nabor)
	vozlisce2 = random.choice(nabor)
	graf.add_edge(vozlisce1, vozlisce2)
	return graf	

def odstrani_povezavo(graf):
	"""
	Odstrani nakljuèno povezavo iz grafa;
	Pazimo, da mora graf, ki ga dobimo, biti povezan.
	"""
	vozlisca = list(graf.keys())
    	vozlisce1 = random.choice(vozlisca)
	seznam_sosedov =  graf[vozlisce1]
	vozlisce2 = random.choice(seznam_sosedov)
	graf.delete_edge(vozlisce1, vozlisce2)
	if graf.is_connected():
		return graf
		
	
def mutacija_vozlisce(graf):
	"""
	Doda vozlisce in mu nato doda nekaj povezav nanj.
	"""	
	dolzina = len(list(graf.keys()))
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
	Na grafu lahko odstranimo, dodamo povezavo, dodamo, 	odstranimo vozlišèe in vsako kombinacijo le teh.
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

def nova_populacija(populacija = zacetna_testna_populacija(), verjetnost = 0.05):
	"""
	Vsak graf iz populacije z neko verjetnostjo spremenimo.
	Za zaèetku za populacijo uporabimo zacetna_testna_populacija()
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
def crossover(n):
	populus = nova_populacija(populacija = zacetna_testna_populacija(), verjetnost = 0.05)
	osebek1 = random.choice(populus)
	osebek2 = random.choice(populus)
	while True:
        subgraf1 = osebek1.random_subgraph(0.5) #vsebuje neko vozlišèe iz osebek1 z verj. 0.5
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

def potomci(populacija = nova_populacija(populacija = zacetna_testna_populacija(), verjetnost = 0.05)):
	nova_populacija = populacija
    	stevilo_parjenj = poisson(t = pop_size)
    		for k in range(stevilo_parjenj):
                starsa = random.sample(populacija, k = 2)
        nova_populacija.append(crossover(n, starsa[0], starsa[1]))
	return nova_populacija
	

def KoncniTestGA(konec):
	populacija = zacetna_testna_populacija()
    i = 1
    while i <= konec:
        populacija = potomci(populacija)
        populacija = mutacija(populacija)
        populacija = testna_populacija(populacija)
        populacija.sort()
        for i in range(len(populacija))
            print("Domneva je ovrzena")
            show(sortPopulation(populacija)[0])
            resitev = sortPopulation(populacija)[0]
            resitev = resitev.to_dictionary()
            return resitev
        i += 1
return "Domneva ni ovrzena."
	
	
	
	
	
	
	
	
	
	