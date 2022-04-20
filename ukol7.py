import re

with open("posta.html", encoding='utf-8') as vstup:
    posta = vstup.read()

posta.replace("\n", " ")

re.sub("\s\s+", "\ ", posta)
reg_vyraz_psc = re.compile("[0-9]{3}\ [0-9]{2}\ [\w(\u00A0|\u0020)]+[ \d]*")
print(reg_vyraz_psc.findall(posta))
