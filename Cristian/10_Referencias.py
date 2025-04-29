'''edad = input ("ingrese su edad: ")

while not edad.isdigit():
    edad = input ("ingrese su edad, solo numeros: ")

edad = int(edad)

#print(edad.isdigit())
#anio_nacimiento = 2023 - edad

print(f"Naciste en el año {2023 - edad}")
'''

# Referencias
palabras = ["casa", "hola","lunes"]
print(palabras)

#copia= palabras # copia toma una referencia a palabra ** puntero **
copia= palabras.copy() # copia toma una referencia a palabra y con .copy() la alojo en otro punto de referencia 
copia.append("chau")
print(copia)
print("*" * 20)
print(palabras)
# Operadores de identidad
print("Identidad")
print(id(copia))
print(id(palabras))
print(copia is palabras) # muestra si copia es puntero de palabras 
