class Auto:
  def __init__(self, spz, znacka, najete_km, volne = True):
    self.spz = spz
    self.znacka = znacka
    self.najete_km = najete_km
    self.volne = volne
  
  def pujc_auto(self):
    if self.volne == True:
      self.volne = False
      print(f"Potvrzuji zapůjčení vozidla.")
    else:
      print(f"Vozidlo není k dispozici.")
      
  def vrat_auto(self, tachometr, pocet_dni):
    self.najete_km = tachometr
    self.pocet_dni = pocet_dni
    self.volne = True
    if pocet_dni < 7:
      cena = pocet_dni * 400
      return print(f"Cena za půjčení je {cena} Kč.")
    else:
      cena = pocet_dni * 300
      return print(f"Cena za půjčení je {cena} Kč.")
  
  def get_info(self):
    print(f"SPZ vozidla je {self.spz} a jedná se o model {self.znacka}.")


auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

volba = input("Jakou značku si přejete půjčit? ")

if volba == "Peugeot":
  auto1.get_info()
  auto1.pujc_auto()
elif volba == "Škoda":
  auto2.get_info()
  auto2.pujc_auto()
else:
  print(f"Tuto značku bohužel nevedeme.")

vraceni_znacka = input("Jakou značku auta vracíte? ")
vraceni_tachometr = input("Jaký je stav tachometru? ")
vraceni_delka = int(input("Kolik dní jste měli auto půjčené? "))

if vraceni_znacka == "Peugeot":
  auto1.vrat_auto(vraceni_tachometr, vraceni_delka)
else:
  auto2.vrat_auto(vraceni_tachometr, vraceni_delka)

