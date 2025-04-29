# Metodos de los Diccionarios
# Los dicts no son ordenados, pero "se pueden ordenar"...

materias = {
    "matematica": [7, 6],
    "literatura": [8, 8.5],
    "historia": [9, 7],
}


print(materias["matematica"]) # accedo al valor
print(materias["matematica"][1]) #accedo a los indices

#print(materias["programacion"]) # KeyError: programacion
materias.get("programacion", "No hay registro") # get recorre el diccionario y vusca el dato ("DATO" , "MENSAJE"  )
print(materias.get("programacion", False))
print(materias.get("historia", False))
print("*" * 50)

print(materias.keys())  # devuelve claves
print("*" * 50)
print(materias.values()) # devuelve los valores de las claves
print("*" * 50)
print(materias.items()) # devuelve clave valor en forma de tuplas

print("*" * 50)
for clave in materias.keys():
    print(f"clave: {clave} - valor: {materias[clave]}") 

print("*" * 50)

for valor in materias.values():
   # print(f"clave: {clave} - valor: {materias[clave]}") 
   #funciona en un solo sentido calve ---> valor Nunca al contrario (valor---> clave)
   print(f"valor: {valor}")

print("*" * 50)

for clave, valor in materias.items(): # desempaueto la tupla
    print(f"clave: {clave} - valor:{valor}")

print("*" * 50)

for par in materias.items(): # forma de ordenar los diccionarios
    print(f"clave: {par[0]} - valor: {par[1]}")
