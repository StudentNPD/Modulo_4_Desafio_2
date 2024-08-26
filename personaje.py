class player:

    def __init__(self):

        self.name = ""
        self.lvl = 1
        self.exp = 0

    def create_hero(self):
        hero_name = input("Ingresa nombre de tu personaje:\n>  ").capitalize()
        self.name = hero_name
