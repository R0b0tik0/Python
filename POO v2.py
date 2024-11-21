from enum import Enum

class Raza(Enum):
    LABRADOR = "Labrador"
    PASTOR_ALEMAN = "Pastor alemán"
    CHIHUAHUA = "Chihuahua"

class Perro:

    def __init__(self, raza, nombre, color):
        self.nombre = nombre
        self.raza = Raza(raza)
        self.color = color

        if self.raza == Raza.LABRADOR:
            self.energia = 70
        elif self.raza == Raza.PASTOR_ALEMAN:
            self.energia = 100
        else:
            self.energia = 50

    def ladrar(self):
        print(self.nombre, "dice guau")
        self.energia -= 5
        
    def moverse(self):
        print(self.nombre, "camina hacia delante")
        self.energia -= 10

    def dormir(self):
        print(self.nombre, "Esta durmiendo")
    
    def info(self):
        print(self.nombre, self.raza, self.color, self.energia)
        
    def atacar(self, otro_perro):
        if self.energia > 0:
            otro_perro.energia -= 10
            print(self.nombre, "ataca a", otro_perro.nombre, "y le quedan",self.energia)
    
    #GETTERS

    def get_nombre(self):
        return self.nombre

"""perro1 = Perro("Chiguagua", "Bob", "Blanco")
perro1.Info()
perro1.ladrar()
perro1.dormir()

class PerroGuia(Perro):
    
    def __init__(self, raza, nombre, color, dueño):
        super().__init__(raza, nombre, color)
        self.__dueño = dueño

    def ladrar(self, dueño):
        print(self.nombre, "ladra y avisa a", dueño)

    def get_dueño(self):
        return self.__dueño
    
    def Info(self):
        print("Este perro pertenece a: ", self.__dueño)
    
perro2 = PerroGuia("Yorkshire", "Juan", "Marron", "Paco")
perro2.ladrar(perro2.get_dueño())

class PerroPolicía(PerroGuia):

    def __init__(self, raza, nombre, color, dueño):
        super().__init__(raza, nombre, color, dueño)
        self.raza = "Pastor Alemán"
        self.energia = 1000

    def BuscarDroga(self):
        print(self.nombre, "busca droga")
        self.energia -= 300

perro3 = PerroPolicía(" " ,"Ben", "Negro", "Poli")
print(perro3.raza)
"""
class Pelea:
    
    def __init__(self,perro1, perro2):
        self.perro1 = perro1
        self.perro2 = perro2
    def pelear(self):
        while self.perro1.energia>0 and self.perro2.energia>0:
            self.perro1.atacar(self.perro2)
            input("Presione enter para continuar")
            self.perro2.atacar(self.perro1)
            if self.perro1.energia <= 0:
                print(self.perro2.nombre ,"ganó")
            elif self.perro2.energia <= 0:
                print(self.perro1.nombre, "ganó")

bobby = Perro("Labrador", "Bobby", "Negro")
bobby.info()
luis = Perro("Pastor alemán", "Luis", "Blanco")
luis.info()            
pelea =  Pelea(bobby, luis)
pelea.pelear