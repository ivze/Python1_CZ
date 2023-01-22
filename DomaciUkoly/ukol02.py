sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}


soucastka = input("Zadej nazev soucastky: ")
mnozstvi = int(input("Zadej mnozstvi: "))

if soucastka in sklad:
    if mnozstvi > sklad[soucastka]:
        print(f'{soucastka} lze prodat pouze omezené množství kusů')
        sklad.pop(soucastka)
    else:
        print(f'poptávku po součástce {soucastka}  lze uspokojit v plné výši')
else:    
    print(f'{soucastka} neni skladem.')
    