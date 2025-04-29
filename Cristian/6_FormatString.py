# Format String

print("comision", 23593, "lunes y miercoels")
#       dato 1    dato 2      dato 3

comision = 23593
mi_cadena = f"Comision {comision} Lunes y Miercoles"
print(mi_cadena)
print(type(mi_cadena))
mi_cadena_2 = f"Hoy es domingo: {7 > 5}"
print(mi_cadena_2)

# Ejemplo
nombre = "Nicolas"
dni = 123456789

#info_limpia = nombre + ' ' + str(dni)
info_limpia = f"{nombre} {dni}"
print(info_limpia)

# Slicing 
# Las cadenas tieneen indice, el indice comienza en 0
# subcadena("cadena", 1,2) "ca"

cadena= "comisión 23593"
#        0123456789...-1
print(cadena[3]) 
print(cadena[2:5])# como arranca en 0 toma del 0 al 4   [desde : hasta(excluido)]
print(cadena[2:12:3]) # [desde : hasta(excluido) : paso]
print(cadena[-1]) # ultima posicion de la cadena    0 1 2 3 4 ..... -1
print(cadena[4:]) # desde la pisicion 4 hasta el final
print(cadena[:10]) # desde el princiopio hasta la posicion 10


# Funcion range()
# Devuelve un rango de numeros 

rango_1 = range(5) # (hasta--excluido) ---> 0 1 2 3 4
print(rango_1)
rango_2 = range(2, 8) # (desde, hasta-exc-) --> 2 3 4 5 6 7
print(rango_2)
rango_3 = range(5, 30, 5) # (desde, hasta-exc-, paso) --> 5 10 15 20 25 
print(rango_3)

# Bucle for
# para x = 1 hasta x = 5 con paso 1 Hacer 
#   <bloque a repetir>
# FinPara

#   control   iterable
for numero in range(5): # range(5) --> 0 1 2 3 4
    print(f"la variable de control vale: {numero}")

print("*" * 30) # multiplico la cadena 30 veces

palabra = "Pyton"
for letra in palabra:
    print(letra)