Import pandas

zvirata = pandas.read_csv("adopce-zvirat.csv", sep=";")
zvirata.info()
zvirata
zvirata.iloc[34][["nazev_cz", "nazev_en"]]