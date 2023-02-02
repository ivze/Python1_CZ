
#hotel

person_price = 850
breakfast_price = 125

def total_price(persons, breakfast = False):

    if breakfast:
        return (person_price * persons) + (breakfast_price * persons)
    else:
        return(person_price * persons)

print(total_price(3))
print(total_price(2, True))

    



