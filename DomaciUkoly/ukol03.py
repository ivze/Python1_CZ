import json
with open('body.json', encoding='utf-8') as soubor:
    text = soubor.read()
body = json.loads(text)
print(body)


prospech = {}

for zak in body:
    if body[zak] > 59:
        prospech[zak] = "pass"
    else:
        prospech[zak] = "fail"


with open('prospech.json', mode='w', encoding='utf-8') as soubor:
    json.dump(prospech, soubor)

print(prospech)
