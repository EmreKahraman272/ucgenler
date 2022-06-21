def ucgendik(x,y,z):
    if (z**2 + x**2 == y**2):
        print("dik üçgen olabilir.")
    if (x**2 + y**2 == z**2):
        print("dik üçgen olabilir.")
    if (y ** 2 + z ** 2 == x ** 2):
        print("dik üçgen olabilir.")
    else:
        print("Dik üçgen değildir")