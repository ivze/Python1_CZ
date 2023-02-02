def secti(a, b):  # parametry
    return a + b

vysledek = secti(8, 5)  # argumenty
print(f"Vysledek je: {vysledek}")


# Ke kazdemu cislu v seznamu pricti 1 pomoci funkce "secti"
seznam_cisel = [2, 5, 9, 8]

# Vysledek jen vypiseme
for cislo in seznam_cisel:
    print(secti(cislo, 1))

# Vysledky ulozime do noveho seznamu
soucty = []
for cislo in seznam_cisel:
    soucty.append(secti(cislo, 1))

print(soucty)