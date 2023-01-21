# Pekarna ma polozky a ceny v korunach
pekarna = {
    "houska": 10, 
    "kolac": 15, 
    "chleba": 40, 
    "muffin": 20,
    "loupak": 20,
    "frgal": 50,
    "frgal": 100
}
#print(pekarna)

#vypis hodnoty
klic = "frgal"
print(f'klic: {klic}, hodnota: {pekarna[klic]}') 
print('klic: ' + klic + ', hodnota: ' + str(pekarna[klic]))

produkt = input("Zadej produkt: ")

#test existence hodnoty

if produkt in pekarna:  # Produkt je v pekarne = klic je ve slovniku (klic je jeden z klicu)
    print(f'{produkt} stoji {pekarna[produkt]} korun.')
else:  # Produkt neni v pekarne = klic neni ve slovniku
    print(f'Bohuzel, produkt {produkt} neprodavame.')

print(pekarna)
pekarna["zavin"] = 150
print(pekarna)

# Pridani zaznamu
pekarna["zavin"] = 150
# Uprava zaznamu
pekarna["muffin"] = 25
print(pekarna)


#pridani zaznamu pormoci metody UPDATE
nove_produkty = {"zavin": 150, "buchta": 150}
pekarna.update(nove_produkty)  # Upravi slovnik pekarna a prida nove_produkty
print(pekarna)

#odebrani zaznamu POP
cena_housky = pekarna.pop("houska")
print(pekarna)
print(cena_housky)

#cyklus pres slovnik

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

# Pri prochazeni pres slovnik prochazime pres jeho klice
for kniha in sales:  
    print(kniha)

for nazev in sales:  
    print(f'Knihy s nazvem {nazev} se prodalo {sales[nazev]} ks.')

# Jake jsou klice slovniku?
print(sales.keys())

# Jake jsou hodnoty slovniku?
print(sales.values())
# Kolik se prumerne prodalo vytisku na knihu?
print(sum(sales.values()) / len(sales))

# pruchod slovniku pomoci metody items()
for nazev, prodano in sales.items():  # Dvojice klic, hodnota
    print(f'Knihy s nazvem {nazev} se prodalo {prodano} ks.')




