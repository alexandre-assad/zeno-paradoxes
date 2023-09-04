def ArrowThrow(aim_distance,speed):
    arrow_pos = 0
    time = 0
    for i in range(aim_distance):
        arrow_pos += 1
        time = arrow_pos/speed
        print(f"A {arrow_pos}m : Avec une vitesse de {speed}m.s, il est {time}s")


while True:
    try:
        spe = int(input("Veuillez choisir la vitesse de la flèche ? \n"))
        ArrowThrow(10,spe)
    except:
        print("Veuillez choisir un nombre entier !")