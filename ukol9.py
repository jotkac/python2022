import pandas

zvirata = pandas.read_csv("adopce-zvirat.csv", sep = ";")

print(zvirata.info())
print(zvirata.iloc[34, [1, 2]])