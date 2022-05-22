import pandas

teploty = pandas.read_csv("temperature.csv")
# print(teploty.info)

praha = teploty[teploty["City"] == "Prague"]
print(praha)

teplota_nad_80 = teploty[teploty["AvgTemperature"] > 80]
print(teplota_nad_80)

evropa_nad_60 = teploty[(teploty["AvgTemperature"] > 60) & (teploty["Region"] == "Europe")]
print(evropa_nad_60)

extrem = teploty[(teploty["AvgTemperature"] > 80) | (teploty["AvgTemperature"] < -20)]
print(extrem)