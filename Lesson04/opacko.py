znamky = {"Petr": {"CJ": 3, "AJ": 2}, "Anna": {"CJ": 1, "AJ": 2}}

jmeno = "Petr"
predmet = "CJ"

print(
    f"Student {jmeno} ma znamku z predmetu {predmet}: {znamky[jmeno][predmet]}"
)

print(predmet, znamky[jmeno][predmet])