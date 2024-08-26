import personaje


# Dar la bienvenida al jugador y solicitar el nombre para su personaje
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("\n        -* Gran Fantasia 1.0 *-")
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("\n \n")

hero = personaje.player()
hero.create_hero()

print(
    f"\nBienvenido {hero.name}, ha comenzado la gran purga de orcos a comenzado, son una terrible invasión... 
    Tienen otras costumbres y malos hábitos, han venido a contaminar nuestro reino con las impurezas de su mundo..."
)

