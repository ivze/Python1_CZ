print("Vitejte u nas v divadle!")  # retezec, string, str

nazev_hry = "Romeo a Julie"

cena_listku = 150

vek = int(input("Kolik vam je let? "))


if vek >= 13:
    pocet_listku = int(input("Zadejte prosim pocet listku: "))
    celkova_cena = cena_listku * pocet_listku

    if pocet_listku >=3:
        zlevnena_cena = celkova_cena * 0.9
        print(f"Celkova cena listku na predstaveni {nazev_hry} je {zlevnena_cena}.")

    else:
        print(f"Celkova cena listku na predstaveni {nazev_hry} je {celkova_cena}.")

else:

    print("Nesplnujete podminku")

