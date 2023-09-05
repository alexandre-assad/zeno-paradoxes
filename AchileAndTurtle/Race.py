from Racer import Racer


def Race(racer1,racer2,iteration):
    print("test_enter")
    for i in range(iteration):
        distance = racer2.position_x - racer1.position_x
        racer1.position_x = racer2.position_x
        racer2.position_x += racer2.movespeed * (distance/racer1.movespeed)
        print(f"Le courreur {racer1.name} est à {racer1.position_x}m, tandis que le courreur {racer2.name} est à {racer2.position_x}m, soit une avance de {abs(racer1.position_x - racer2.position_x)}")



while True:
    try:
        iterations = int(input("Combien d'itération voulez vous ? \n"))
        Race(Racer("Achille",0,14), Racer("Tortue",10,8),iterations)
    except:
        print("Veuillez rentrer un nombre entier ! \n")
