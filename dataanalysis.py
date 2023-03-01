import pandas as pd


# --------------- party attention ------------------

scraped = pd.read_csv('/Users/joanabayraktar/Desktop/Arbeit/2.0 bayernGraph/all_data.csv', sep=",")
short = scraped["title"][0:20]

CSU = scraped.loc[scraped["title"].str.contains("CSU", case=True)]
SPD = scraped.loc[scraped["title"].str.contains("SPD", case=True)]
AfD = scraped.loc[scraped["title"].str.contains("AfD|Alternative für Deutschland|AFD|afd", case=True)]
FDP = scraped.loc[scraped["title"].str.contains("FDP|Freie Demokraten", case=True)]
GRÜNE = scraped.loc[scraped["title"].str.contains("Grüne|GRÜNE|GRUENE|Gruene", case=True)]
FW = scraped.loc[scraped["title"].str.contains("FW |Freie Wähler", case=True)]

cCSU = len(CSU)
cSPD = len(SPD)
cAfD = len(AfD)
cFDP = len(FDP)
cGRÜNE = len(GRÜNE)
cFW = len(FW)

party_attention = pd.DataFrame({'Partei':['CSU', 'SPD', 'AfD', "FDP", "GRÜNE", "FW"], 'Anzahl':[cCSU, cSPD, cAfD, cFDP, cGRÜNE, cFW]})

party_attention.to_csv("party_attention.csv", index=True)

CSU = CSU.drop(columns=["content", "authors", "subtitle", "region_media"])
SPD = SPD.drop(columns=["content", "authors", "subtitle", "region_media"])
FDP = FDP.drop(columns=["content", "authors", "subtitle", "region_media"])
GRÜNE = GRÜNE.drop(columns=["content", "authors", "subtitle", "region_media"])
AfD = AfD.drop(columns=["content", "authors", "subtitle", "region_media"])
FW = FW.drop(columns=["content", "authors", "subtitle", "region_media"])

CSU.to_csv("CSU.csv")
SPD.to_csv("SPD.csv")
FDP.to_csv("FDP.csv")
GRÜNE.to_csv("GRÜNE.csv")
AfD.to_csv("AfD.csv")
FW.to_csv("FW.csv")

# --------------- Anzahl Artikel ------------------

count_all = len(scraped)