def StoneThrow(distance,iteration):
    position_x = 0
    movespeed = distance/2
    for i in range(iteration):
        position_x += movespeed
        movespeed /= 2
        print(f"Le caillou est à {position_x}m, l'arbre à {distance}m, soit {abs(position_x-distance)}m d'écart")


while True:
    try:
        ite = int(input("Veuillez choisir le nombre d'itérations ? \n"))
        StoneThrow(8,ite)
    except:
        print("Veuillez choisir un nombre entier !")