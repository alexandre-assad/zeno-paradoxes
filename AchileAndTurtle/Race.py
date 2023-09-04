from Racer import Racer


def Race(racer1,racer2,iteration):
    for i in range(iteration):
        racer1.position_x += racer1.movespeed
        racer2.position_x += racer2.movespeed
        racer1.movespeed /= 2
        racer2.movespeed /= 2
        print(f"Le courreur {racer1.name} est à {racer1.position_x}m, tandis que le courreur {racer2.name} est à {racer2.position_x}m, soit une avance de {abs(racer1.position_x - racer2.position_x)}")



while True:
    try:
        iterations = int(input("Combien d'itération voulez vous ? \n"))
        Race(Racer("Achille",0,10), Racer("Tortue",10,5),iterations)
    except:
        print("Veuillez rentrer un nombre entier ! \n")
