sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}


soucastka = input("Zadej nazev soucastky: ")
mnozstvi = int(input("Zadej mnozstvi: "))

if soucastka not in sklad:
    print(f'{soucastka} neni skladem.')

if soucastka in  sklad.items() >= mnozstvi in sklad:
    print(f'{soucastka} poptávku lze uspokojit v plné výši')
    sklad.pop(soucastka)

else:    
    soucastka in  sklad.items() < mnozstvi in sklad
    print(f'{soucastka} lze prodat pouze omezené množství kusů')
