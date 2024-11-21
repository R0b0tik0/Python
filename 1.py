#print("Hola Mundo")

#Variables

"""Cadenas por defecto (str)

int numeros enteros, positivos y negativos
float, con decimales, positivos y negativos
complex numeros con parte real e imaginaria (i)

Bool (true o false)

 

#nombre = input("Introduce tu nombre: ")

año_que_naciste = int(input("Introduce el año en el que naciste: "))

#color_favorito = input("Introduce tu color favorito: ")

#respuesta = (input("Eres mayor de edad?: ")).strip().lower() 
#mayor_de_edad = (respuesta == "si")

respuesta = (input("Tienes gafas?: ")).strip().lower()
#gafas = (respuesta == "si")

#print(nombre,año_que_naciste,color_favorito,mayor_de_edad,gafas)

#Operaciones

año_actual = int(input("En qué año estamos?: ")
edad = año_actual-año_que_naciste
print(edad)

mayor_de_edad = (edad >=18)

#Estructura de control

if respuesta == "si":
    gafas = True

elif respuesta == "no":
    gafas = False

if gafas:
    color_gafas = (input("De qué color son tus gafas?: " ))

else:
    color_ojos = (input("De qué color son tus ojos?: "))

"""
#dividendo = 40.0
#divisor = 20.0
#division = dividendo / divisor
#modulo = dividendo % divisor
#print(division, modulo)

"""def es_bisiesto(año_general):
    if (año_general % 4 == 0):
        return True
    else:
        return False

año = int(input("Introduce un año: "))
if es_bisiesto(año):
    print("Es bisiesto")
else:
    print("No es bisiesto")
    
    
"""

# Bucle for y while


resultado = 0
for i in range(0,11,2):
    resultado += i

print(resultado)

alumnos = ["Jaime", "Candela", "Lucas", "Sergio"]

for i in alumnos:
    letras = len(i)
    print(i, "tiene", letras, "letras")

