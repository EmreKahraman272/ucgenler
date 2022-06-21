def ucgenkenar(x,y,z):
    if (x-y < z < x+y):
        return True
    else:
        return False






def ucgencevre(n,):
    n = (x + y + z)
    print(n , "üçgenin çevresidir.")




def ucgendik(x,y,z):
    if (z**2 + x**2 == y**2):
        print("dik üçgen olabilir.")
    elif (x**2 + y**2 == z**2):
        print("dik üçgen olabilir.")
    elif (y ** 2 + z ** 2 == x ** 2):
        print("dik üçgen olabilir.")
    else:
        print("Dik üçgen değildir")






x = int(input("1. kenarı giriniz."))
y = int(input("2. kenarı giriniz."))
z = int(input("3. kenarı giriniz."))
n = (x + y + z)
if ucgenkenar(x,y,z) == True:
    ucgencevre(n)
    ucgendik(x,y,z)
