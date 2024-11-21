#Adivinar un numero

import random

inicio = int(input("En qué número empezamos?: "))
fin = int(input("En cual terminamos?:  "))
numero = random.randint(inicio,fin)
intentos = int(input("Cuantos intentos necesitas?: "))

print("Adivina el número")
ganado = False
while intentos > 0 and ganado == False:
    print("Te quedan",intentos, "intentos")
    guess = int(input("Introduce un número: "))
    if guess == numero:
        ganado = True
    elif guess < numero:
        print("Te has quedado corto")
    else:
        print("Te has pasado")
    intentos -= 1
if intentos == 0 and ganado == False:
    print("El número era el", numero)
    input("Presione enter para salir")

elif intentos >= 1 and ganado == True:
    print("Has ganado")
    input("Presione enter para salir")
    