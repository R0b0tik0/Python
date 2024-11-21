def grados_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

entrada = int(input("Introduce los grados Celsius: "))
resultado = grados_fahrenheit(entrada)
print("Son", resultado, "grados Fahrenheit")

# Para que si lo ejecutas fuera del Visual Studio no se cierre automaticamente
input("Presione Enter para salir")