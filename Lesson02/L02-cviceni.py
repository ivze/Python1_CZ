""" Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). Vypiš obsah slovníku pomocí funkce print(). """

vysvedceni = {
    "cestina": 1, 
    "matematika": 2, 
    "telocvik": 4, 
}

print(vysvedceni)

""" Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujícím slovníku najdeš tři knihy a u každé z nich je počet prodaných kusů. """

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc,ktera me zabila"] = 0
sales["Vrah zavolá v deset"] = 5691

print(sales)

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

cisloListku = int(input("Zadej cislo listku: "))
if cisloListku in tombola:
    print(f'{cisloListku} vyhrava {tombola[cisloListku]}')
    tombola.pop(cisloListku)
else: 
    print(f'Bohuzel, {cisloListku} nevyhral.')

print(tombola)