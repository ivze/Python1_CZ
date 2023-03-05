# ukol-07

class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            return "Potvrzuji půjčení vozidla"
        else:
            return "Vozidlo není k dispozici"
    
    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka}, Typ vozidla: {self.typ_vozidla}"
    

Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

vozy = {"Škoda": Skoda, "Peugeot": Peugeot}

jake_auto = input("Jake auto chcete? (k dispozici Peugeot nebo Škoda) ")

print(vozy[jake_auto].get_info())
print(vozy[jake_auto].pujc_auto())