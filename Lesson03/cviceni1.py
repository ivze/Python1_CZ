# stahnuti dat, otevreni a prevod na json
# metoda read = umí soubor načíst do jednoho řetězce. 
# řetězec se preda funkci loads z modulu json, ta ho přečte a pokud jsou v něm data ve formátu JSON, převede je na Python slovníky.
# load = umí přečíst JSON přímo z otevřeného souboru


import json
# with open('absolventi.json', encoding='utf-8') as soubor:
#     data = soubor.read()
# absolventi = json.loads(data)
# # print(absolventi)
# # print (type(json.loads(data)))
# print(absolventi[0])

# zapis dat = fukce dump


# hodiny = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
# # with open('hodiny.json', mode='w', encoding='utf-8') as soubor:
# #     json.dump(hodiny, soubor)
# print(hodiny)
# # print(json.dumps(hodiny))

# import json
# with open('absolventi.json', encoding='utf-8') as soubor:
#     absolventi = json.load(soubor)
# print(absolventi)

# import requests
# import json
# response = requests.get('https://api.kodim.cz/python-data/people')
# data = json.loads(response.text)
# print(data)

import requests

import json

response = requests.get('https://api.kodim.cz/python-data/people')
data = json.loads(response.text)

# 1
# Zjistěte kolik lidí celkem seznam obsahuje.
print(len(data))

# Zjistěte jaké všechny informace máme o jednotlivých osobách.
for person in data:
    print(list(person.keys()))


# Zjistěte, kolik je v souboru mužů a žen.
zeny = []
muzi = []
for person in data:
    pohlavi = person["gender"]
    if pohlavi == 'Female':
        zeny.append(person)
    else:
        muzi.append(person)

print(f"Pocet muzu: {len('')}")
print(f'Pocet zen: {len(zeny)}')

