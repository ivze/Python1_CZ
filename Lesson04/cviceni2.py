# Zadej slovo: ahoj
# ********
# * ahoj *
# ********

def ramecek (slovo):
    print((len(slovo) + 4) * '*')
    print(f"* {slovo}* ")
    print((len(slovo) + 4) * '*')

slovo = input("zadej slovo ")
ramecek = (slovo)
print(ramecek)

