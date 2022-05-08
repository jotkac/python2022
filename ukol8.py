from datetime import datetime

zacatek_drazsiho_obdobi = datetime(2021, 7, 1)
konec_drazsiho_obdobi = datetime(2021, 8, 10)
konec_levnejsiho_obdobi = datetime(2021, 8, 31)
vybrane_datum = input("Na který den chcete zakoupit vstupenku? ")
pocet_osob = int(input("Kolik vstupenek si přejete? "))

vybrane_datum = datetime.strptime(vybrane_datum, "%d. %m. %Y")

if vybrane_datum >= zacatek_drazsiho_obdobi and vybrane_datum <= konec_drazsiho_obdobi:
  vysledek = pocet_osob * 250
  print(f"Cena za vstupenky je {vysledek} Kč.")
elif vybrane_datum > konec_drazsiho_obdobi and vybrane_datum <= konec_levnejsiho_obdobi:
  vysledek = pocet_osob * 180
  print(f"Cena za vstupenky je {vysledek} Kč.")
else:
  print("Tento den je letní kino bohužel zavřené.")
