import json
with open('body.json', encoding='utf-8') as soubor:
    text = soubor.read()
body = json.loads(text)
print(body)


prospech = {
    "Daniel Svoboda": "pass",
   "Anežka Benešová": "fail",
   "Andrea Vanková": "fail",
   "Robin Blažek": "pass",
   "Renáta Tichá": "pass",
   "Matyáš Vanek": "fail",
   "Tereza Procházková": "fail",
   "Luboš Cerný": "pass",
   "Vasyl Novotný": "pass",
   "Jaroslav Polák": "fail",
   "Dušan Kríž": "pass",
   "Vlasta Kadlecová": "fail",
   "Zdenka Soukupová": "pass",
   "Igor Krejcí": "pass",
   "Stanislav Vanek": "pass",
   "Julie Poláková": "fail",
   "Veronika Fialová": "fail",
   "Kvetoslava Dvoráková": "fail",
   "Ladislav Cermák": "pass",
   "Dana Marková": "pass",
   "Miloš Horák": "pass",
   "Štefan Jelínek": "fail",
   "Miloš Veselý": "fail",
   "Aleš Kríž": "fail",
   "Marcela Machová": "fail",
   "Blanka Kucerová": "pass",
   "Šárka Marešová": "pass",
   "Dalibor Kadlec": "fail",
   "Robert Pospíšil": "fail"
   }


with open('prospech.json', mode='w', encoding='utf-8') as soubor:
    soubor.write(json.dumps(body))
print(json.dumps(prospech))