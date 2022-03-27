def overeni_cisla(telefonni_cislo):
  if len(telefonni_cislo) == 9 or 13:
    return True
  else: return False

def cena_zpravy(zprava):
  cena_za_jednu = 3
  delka_zpravy = len(zprava)
  pocet_zprav = round(delka_zpravy/180)
  if (delka_zpravy % 180) != 0:
    pocet_zprav += 1
  return cena_za_jednu * pocet_zprav


telefonni_cislo = input("Zadejte telefonní číslo: ")
overeni_cisla(telefonni_cislo)
if telefonni_cislo == False:
  print("Zadali jste neplatné číslo.")
else: zprava = input("Zadejte zprávu: ")

print(f"Cena za zprávu je {cena_zpravy(zprava)} Kč.")



