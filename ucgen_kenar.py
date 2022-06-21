def ucgenkenar(x,y,z):
    x = int(input("1. kenarı giriniz."))
    y = int(input("2. kenarı giriniz."))
    z = int(input("3. kenarı giriniz."))
    if (x-y < z < x+y):
        return True
    else:
        return False