
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

prumer_den = []
for x in teploty:
    a = 0
    b = 0
    for y in x:     
        a = a + y
        b = b + 1
    prumer_den.append(a/b)
print(prumer_den)


# # 	2. Vytvoř seznam ranních teplot.


def ranni_teploty(nums, n):
   result = [i.pop(n) for i in nums]
   return result 
n = 0
print(ranni_teploty(teploty, n))


# # 	3. Vytvoř seznam nočních teplot.

def nocni_teploty(nums, n):
   result = [i.pop(n) for i in nums]
   return result 
n = 2
print(nocni_teploty(teploty, n))


# # Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.


x = [row[1] for row in teploty]
y = [row[3] for row in teploty]
print(x)
print(y)






