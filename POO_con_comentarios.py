from enum import Enum

# Definición de una enumeración para las razas de perros
class Raza(Enum):
    LABRADOR = "labrador"
    PASTOR_ALEMAN = "pastor aleman"
    CHIHUAHUA = "chihuahua"
    HUSKY = "husky"

# Definición de la clase Perro
class Perro:

    # Inicializador de la clase Perro
    def __init__(self, raza, nombre, color):
        self.nombre = nombre
        self.raza = Raza(raza)
        self.color = color

        # Asignación de la energía según la raza
        if self.raza.value == "labrador":
            self.energia = int(70)
        elif self.raza.value == "pastor aleman":
            self.energia = int(100)
        elif self.raza.value == "chihuahua":
            self.energia = int(50)
        else:
            self.energia = int(80)

    # Método para simular el ladrido del perro
    def ladrar(self):
        print(self.nombre, "dice guau")
        self.energia -= 5
        
    # Método para simular el movimiento del perro
    def moverse(self):
        print(self.nombre, "camina hacia delante")
        self.energia -= 10

    # Método para simular que el perro está durmiendo
    def dormir(self):
        print(self.nombre, "Esta durmiendo")
    
    # Método para mostrar la información del perro
    def info(self):
        print(self.nombre, self.raza.value, self.color, self.energia)
        
    # Método para que el perro ataque a otro perro
    def atacar(self, otro_perro):
        if self.energia > 0:
            otro_perro.energia -= self.energia // 2
            self.energia -= otro_perro.energia // 4
            print(self.nombre, "ataca a", otro_perro.nombre, "y le quedan",self.energia)
    
    # GETTERS
    def get_nombre(self):
        return self.nombre

# Definición de la clase PerroGuia que hereda de Perro
class PerroGuia(Perro):
    
    # Inicializador de la clase PerroGuia
    def __init__(self, raza, nombre, color, dueño):
        super().__init__(raza, nombre, color)
        self.__dueño = dueño

    # Método para que el perro guía ladre y avise al dueño
    def ladrar(self, dueño):
        print(self.nombre, "ladra y avisa a", dueño)

    # Método getter para obtener el dueño
    def get_dueño(self):
        return self.__dueño
    
    # Método para mostrar la información del perro guía
    def info(self):
        super().info()
        print("Este perro pertenece a: ", self.__dueño)
        
    # Método para que el perro guía ataque a otro perro
    def atacar(self, otro_perro):
        if self.energia > 0:
            otro_perro.energia -= self.energia // 4
            self.energia -= otro_perro.energia // 2
            print(self.nombre, "ataca a", otro_perro.nombre, "y le quedan",self.energia)
    
# Definición de la clase PerroPolicía que hereda de PerroGuia
class PerroPolicía(PerroGuia):

    # Inicializador de la clase PerroPolicía
    def __init__(self, nombre, color, dueño):
        super().__init__(Raza.PASTOR_ALEMAN, nombre, color, dueño)
        self.energia = 200
        
    # Método para que el perro policía busque drogas
    def BuscarDroga(self):
        print(self.nombre, "busca droga")
        self.energia -= 50
        
    # Método para que el perro policía ataque a otro perro
    def atacar(self, otro_perro):
        if self.energia > 0:
            otro_perro.energia -= self.energia
            print(self.nombre, "ataca a", otro_perro.nombre, "y le quedan",self.energia)
        
        # Método para mostrar la información del perro policía
        def info(self):
            super().info()

# Definición de la clase Pelea
class Pelea:
    
    # Inicializador de la clase Pelea
    def __init__(self,perro1, perro2):
        self.perro1 = perro1
        self.perro2 = perro2
        
    # Método para simular la pelea entre dos perros
    def pelear(self):
        print("Se van a enfrentar", self.perro1.nombre, "contra" ,self.perro2.nombre)
        while self.perro1.energia>0 and self.perro2.energia>0:
            self.perro1.atacar(self.perro2)
            input("Presione enter para continuar")
            self.perro2.atacar(self.perro1)
            if self.perro1.energia <= 0:
                print(self.perro2.nombre ,"ganó")
            elif self.perro2.energia <= 0:
                print(self.perro1.nombre, "ganó")

# Creación de instancias de Perro y ejecución de métodos
bobby = Perro("labrador", "Bobby", "Negro")
bobby.info()

luis = Perro("pastor aleman", "Luis", "Blanco")
luis.info()

bruno = PerroGuia("husky","Bruno","blanco", "Paco")
bruno.info()

michael = PerroPolicía("Michael", "Negro", "Poli")
michael.info()

# Creación de instancias de Pelea y ejecución del método pelear
pelea = Pelea(bobby, luis)
pelea.pelear()

pelea2 = Pelea(michael, luis)
pelea2.pelear()

pelea3 = Pelea(luis, bruno)
pelea3.pelear()
