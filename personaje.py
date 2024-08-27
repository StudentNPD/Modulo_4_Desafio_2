class Personaje():
    
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.nivel = 1 
        self.experiencia = 0

    def __lt__(self, other):
        return self.nivel < other.nivel
    
    def __gt__(self, other):
        return self.nivel > other.nivel
    
    def __eq__(self, other): 
        return self.nivel == other.nivel
    
    
    def mostrar_probabilidad(self,other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else: 
            return 0.5
        
    @property    
    def estado(self):
        return f"""
nombre: {self.nombre}
nivel: {self.nivel}
experiencia: {self.experiencia}"""    
        

    @estado.setter
    def estado(self, exp:int):
        temp_exp = self.experiencia + exp
        if self.nivel==1 and exp<0 and (temp_exp)<0:
            print("1")
            self.nivel=1 
            self.experiencia=0    
        elif self.nivel>=1 and exp>=0 and (temp_exp)<100:
            print("2")
            #self.nivel=1 
            self.experiencia=self.experiencia + exp
        elif self.nivel>=1 and exp>=0 and (temp_exp)>=100:
            print("3")
            self.nivel+=1
            #print(temp_exp)
            #print((temp_exp - 100 ) )
            self.experiencia=(temp_exp - 100 ) 
        if self.nivel==1 and exp<0 and (temp_exp)>0:
            print("4")
            #self.nivel=1 
            self.experiencia=temp_exp

    @staticmethod  
    def mostrar_opciones(probabilidad_de_ganar):
        return int(input(f"""
Con tu nivel actual, tienes {probabilidad_de_ganar * 100}% de probabilidades de ganarle al Orco.                    
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50. 
¿Qué deseas hacer?
1. Atacar
2. Huir                
"""))
