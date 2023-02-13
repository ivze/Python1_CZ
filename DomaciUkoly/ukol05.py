
teploty=[
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]


# # 	1. Vytvoř seznam průměrných teplot pro každý den.

prumer_den = [sum(teplota)/len(teplota) for teplota in teploty]
print(prumer_den)


# # 	2. Vytvoř seznam ranních teplot.

ranni_teploty = [column[0] for column in teploty]
print(ranni_teploty)


# # 	3. Vytvoř seznam nočních teplot.

nocni_teploty = [column[3] for column in teploty]
print(nocni_teploty)


# # Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

poledni_nocni_teploty = [[column[1], column[3]] for column in teploty]
print(poledni_nocni_teploty)







