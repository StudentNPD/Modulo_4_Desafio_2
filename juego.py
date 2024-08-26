import personaje


# Dar la bienvenida al jugador y solicitar el nombre para su personaje
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("\n        -* Gran Fantasia 1.0 *-")
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("\n \n")

hero = personaje.player()
hero.create_hero()
