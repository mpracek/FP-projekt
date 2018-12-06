def generiraj_graf(graf):
    povezava = []
    for vozlisce in graf:
        for sosed in graf[vozlisce]:
            povezava.append((vozlisce, sosed))

    return povezava

print(generiraj_graf(graf))


def nepovezano(graf):
    """ Vrne nepovezana vozlišča, če so naš ne zanima"""
    izolirano = []
    for vozlisce in graf:
        if not graf[vozlisce]:
            izolirano += vozlisce
    return izolirano

class Graf(object):

    def __init__(self, graf_slovar=None):
        """ ustvari objekt graf 
            če ga grafa slovarja oziroma je None, bo ustvarjen nov    
	"""
        if graf_slovar == None:
            graf_slovar = {}
        self.__graf_slovar = graf_slovar


    def vozlisca(self):
        """ vrne vozlišča grafa """
        return list(self.__graf_slovar.keys())

    def povezave(self):
        """ vrne povezava grafa """
        return self.__generate_povezava()

    def add_vozlisce(self, vozlisce):
        """ če vozlisce "vozlisce" ni v
            self.__graf_slovar, bo ključ "vozlisce" dodam v slovar s praznim seznamom.. 
            Drugače ne naredi nič. 
        """
        if vozlisce not in self.__graf_slovar:
            self.__graf_slovar[vozlisce] = []

    def add_povezava(self, povezava):
        """ Privzamemo da je povezava množica, tuple or seznam; 
            med vozliščema je lahko več povezav povezava! 
        """
        povezava = set(povezava)
        vozlisce1 = povezava.pop()
        if povezava:
            vozlisce2 = povezava.pop()
        else:
            vozlisce2 = vozlisce1
        if vozlisce1 in self.__graf_slovar:
            self.__graf_slovar[vozlisce1].append(vozlisce2)
        else:
            self.__graf_slovar[vozlisce1] = [vozlisce2]

	def __generate_povezava(self):
            """ Statistična metoda s katero generiramo povezave grafa "graf".
	        Povezave so predstaveljene kot množice z enim (povezava iz A v A)
	    	ali dvemi vozlišči.
            """
        	povezava = []
        	for vozlisce in self.__graf_slovar:
            		for sosed in self.__graf_slovar[vozlisce]:
                		if {sosed, vozlisce} not in povezava:
                    			povezava.append({vozlisce, sosed})
             return povezava
    	def find_izolirano_vozlišče(self):
             """ vrne seznam izoliranih vozlišč, to je tistih brez povezav vozlišče. """
            graf = self.__graf_slovar
      	    izolat = []
        	for vozlisce in graf:
           	 	print(izolat, vozlisce)
            		if not graf[vozlisce]:
                		izolat += [vozlisce]
        	return izolat
