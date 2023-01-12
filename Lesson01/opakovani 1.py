print("Vitejte u nas v divadle!")  # retezec, string, str

nazev_hry = "Romeo a Julie"

cena_listku = 150
pocet_listku = 5

celkova_cena = cena_listku * pocet_listku

print(f"Cena listku {celkova_cena}")

# nacteni od uzivatele
pocet_listku = int(input("Zadejte prosim pocet listku: "))

#podminka

# Pokud je pocet listku alespon 3, dostane zakaznik slevu 10%
if pocet_listku >= 3:
    zlevnena_cena = celkova_cena * 0.90
    print(
        f"Celkova cena listku na predstaveni {nazev_hry} je {zlevnena_cena}."
        f"Usetrili jste 10% oproti puvodni cene {celkova_cena}"
    )
else:
    print(f"Celkova cena listku na predstaveni {nazev_hry} je {celkova_cena}.")


# Spojovani sekvenci

print("Dobry" + " " + "den")
print("Dobry den")

pozdrav = "Dobry den"
jmeno = "Andy"
print(f"{pozdrav} {jmeno}")  # spojeni retezcu pomoci f-stringu

venecky = [1, 2, 4, 1, 6, 0, 1]
print(venecky + [0, 1, 2, 0, 2, 0, 5])


venecky = [1, 2, 4, 1, 6, 0, 1]

#SLICING 
# 
# # print(venecky[zacatek:konec+1])
# Od pondeli do patka
print(venecky[0:5])

# Od utery do nedele
print(venecky[1:7])
# Od utery do konce sekvence (do nedele)
print(venecky[1:])

# Od zacatku do ctvrtka
print(venecky[:4])

# Od zacatku do konce
print(venecky[:])


#METODY NA RETEZCICH

print('  martin   ')
print('  martin   '.strip())  # zbaveni mezer na zacatku a na konci

print('martin'.upper())  # prevod na velka pismena
print('MARTIN'.lower())  # prevod na mala pismena






