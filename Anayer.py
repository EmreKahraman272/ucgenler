def ucgenkenar(x,y,z):
    if (x-y < z < x+y) and (z-y < x < z+y) and (x-z < y < x+z)  :
        return True
    else:
        return False






def ucgencevre(x,y,z):
    return (x+y+z)




def ucgendik(x,y,z):
    if (z**2 + x**2 == y**2):
        return True
    elif (x**2 + y**2 == z**2):
        return True
    elif (y ** 2 + z ** 2 == x ** 2):
        return True
    else:
        return False












x = int(input("1. kenarı giriniz."))
y = int(input("2. kenarı giriniz."))
z = int(input("3. kenarı giriniz."))
n = (x + y + z)
if ucgenkenar(x,y,z):
    print("Üçgendir.")
    print(ucgencevre(x, y, z), "üçgenin çevresidir.")
    if ucgendik(x, y, z):
        print("Dik üçgendir.")
    else:
        print("Dik üçgen değildir.")
else:
    print("Üçgen değildir.")
