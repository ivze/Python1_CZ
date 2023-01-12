#zadani

#program se zeptal uživatele i na věk, a ověřil, že má alespoň 13 let. Pokud nemá alespoň 13 let, nezeptá se už na počet lístků, a skončí (tj. nákup neproběhne).


print("Vitejte u nas v divadle!")

nazev_hry = "Romeo a Julie"

cena_listku = 150
vek_zakaznika = int(input("Zadejte prosim vas vek: ")) 

# Pokud ma zakaznik dostatecny vek, proved prodej. 
# V opacnem pripade program skoci za blok podminky a skonci.
if vek_zakaznika >= 13:  
    pocet_listku = int(input("Zadejte prosim pocet listku: "))
    celkova_cena = cena_listku * pocet_listku

    # Pokud je pocet listku alespon 3, dostane zakaznik slevu 10%
    if pocet_listku >= 3:
        zlevnena_cena = celkova_cena * 0.90
        print(
            f"Celkova cena listku na predstaveni {nazev_hry} je {zlevnena_cena}kc. "
            f"Usetrili jste 10% oproti puvodni cene {celkova_cena}kc."
        )
    else:
        print(f"Celkova cena listku na predstaveni {nazev_hry} je {celkova_cena}kc.")