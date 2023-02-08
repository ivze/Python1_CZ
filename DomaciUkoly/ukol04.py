def overeni_cisla(telefon):
 
    if len(telefon) == 13 and telefon.startswith("+420") == True:   
        return True
    elif  len(telefon) == 9:
        return True
    else:
        return False


def cena_SMS(s):

    cena_180_znaku = 3
    kolik_znaku = len(s)
    kolik_znaku % 180 != 0
    cena = kolik_znaku / 180
    cena_SMS = int (cena * cena_180_znaku)
    return cena_SMS

telefon_uzivatel = input("Zadej cislo: ")

if overeni_cisla(telefon_uzivatel) == False:
    print("Spatne cislo.")
else:
    SMS = input("Napis sms: ")
    print(f"Cena SMS je {cena_SMS(SMS)} Kč.")