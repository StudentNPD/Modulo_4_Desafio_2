#import personaje


## Dar la bienvenida al jugador y solicitar el nombre para su personaje
#print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#print("\n        -* Gran Fantasia 1.0 *-")
#print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#print("\n \n")

#hero = personaje.player()
#hero.create_hero()


#print(
#    f"\nBienvenido {hero.name}, ha comenzado la gran purga de orcos a comenzado, son una terrible invasión... 
#    Tienen otras costumbres y malos hábitos, han venido a contaminar nuestro reino con las impurezas de su mundo...\n"
#)

#hero.mostrar_estado()


#print("¡Oh no!, ¡Ha aparecido un Orco!")

#orco = Personaje("orco")


from personaje import Personaje
import random


nombre = input("""
¡Bienvenido a Gran Fantasía!

Por favor indique nombre de su personaje:\n                      
> """)

heroe = Personaje(nombre)

print(heroe.estado)

print("\n¡Oh no!, ¡Ha aparecido un Orco!")

orco = Personaje("orco")

probabilidad_de_ganar = heroe.mostrar_probabilidad(orco)

while True:
    try:
        opcion_orco = int(heroe.mostrar_opciones(probabilidad_de_ganar))
        if opcion_orco not in [1, 2]:
            raise ValueError
        break
    except ValueError:
        print("Por favor, ingrese solo 1 o 2.")


while opcion_orco == 1:
    if random.uniform(0,1) < probabilidad_de_ganar :
        print("""
¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!
""")
        heroe.estado = 50
        #print(f"Estado del Heroe: {heroe.estado}")
        orco.estado = -30
        #print(f"Estado del Orco: { orco.estado}")
    else: 
        print("""
¡Oh no! ¡El orco te ha ganado!
¡Has perdido 30 puntos de experiencia!        
    """)
        heroe.estado = -30
        orco.estado = 50
        
    print(f"Estado del Heroe: {heroe.estado}")
    print(f"Estado del Orco: { orco.estado}")

    while True:
        try:
            opcion_orco = int(heroe.mostrar_opciones(probabilidad_de_ganar))
            if opcion_orco not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Por favor, ingrese solo 1 o 2.")



if opcion_orco==2:
    print("¡Has huido! El orco ha quedado atrás.")
                
#    print(heroe.estado)
#    print(orco.estado)
