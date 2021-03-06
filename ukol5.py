class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  
  def get_info(self):
    return f"{self.nazev}, {self.zanr}"

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  
  def get_info(self):
    return super().get_info() + f", {self.delka}"

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody
  
  def get_info(self):
    return super().get_info() + f", {self.pocet_epizod}, {self.delka_epizody}"

lotr = Film("Pán prstenů", "fantasy", "3 hod")
peakyblinders = Serial("Peaky Blinders", "krimi", 6, "55 min")
print(lotr.get_info())
print(peakyblinders.get_info())

