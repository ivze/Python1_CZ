import re

# 1. Datum
platny_regularni_vyraz = re.compile(r"\d\d?(.|. |\/)\d\d?(.|. |\/)\d{4}")

# 2. Adresa
posledni_radek_adresy_regularni_vyraz = re.compile(r"\d{3} \d{2} +(\w+ \w+ \w+|\w+ \w+|\w+)")

