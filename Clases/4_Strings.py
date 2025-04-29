# Metodo de los Strings LOS METODOS SON FUNCIONES
#
#

cadena = "codo a codo"
comision= "23593"

# Metodos vs Funciones (Ejecucion)
print(cadena) # Funcion (dato)

print(cadena.upper()) #dato.metodo() upper= MAYUSCULAS: pasa todo el vector a mayusculas
print(cadena.capitalize()) # 1ra letra en mayuscula
print(cadena.title()) # primera 1ra letra mayuscula cada palabra

'''var= input("ingrese algo: ")
print(var.upper())'''

print(comision.isdigit()) # verifica que la cadena sean todos numeros (solo sirve en STR) ***devuelve un true o false***
# https://peps.python.org/pep-0008/      malas practicas de programacion 
# if comision.isdigit() == True: mala practica
# if comision.isdigit() if True: mala practica II
if comision.isdigit(): # si es true
    print("son todos numeros")
else: # si es False
    print("tiene alguna letra")

if cadena.isalpha(): # verifica si son todas letras, sin espacios, ni numeros, ni simbolos
    print("son todas letras")
else:
    print("tiene algun espacio o numero")
    