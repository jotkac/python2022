soubor = input("Zadejte název souboru: ")
with open(soubor, encoding="utf-8") as vstup:
  auta = vstup.readlines()
auta = [auto.replace(",", ".") for auto in auta]
auta = [auto.split() for auto in auta]

auta = [[auto[0], float(auto[1])] for auto in auta]
soucet = sum(auto[1] for auto in auta)
print(f"Auta najela celkem {soucet} km.")