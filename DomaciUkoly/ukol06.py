import re

# 1. Platny vyraz
platny_regularni_vyraz = re.compile(r"\d\d?(.|. |\/)\d\d?(.|. |\/)\d{4}")

# 2. Posledni radek adresy
posledni_radek_adresy_regularni_vyraz = re.compile(r"\d{3} \d{2} +(\w+ \w+ \w+|\w+ \w+|\w+)")

