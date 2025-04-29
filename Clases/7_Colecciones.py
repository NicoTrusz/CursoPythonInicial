# Colecciones
# Listas, tuplas y diccionarios (tambien existen sets y frozensets)
#
'''
# calculo promedios
cant_nros = input("Ingrese cantidad: ")
acumulador = 0

for n in range(int (cant_nros)) :
    valor = input("ingrese valor: ")
    acumulador += float(valor)

print(f"el promedio es: {acumulador / int(cant_nros)}")
'''
# Listas
# Sintaxis  valores entre cochetes y separados por comas 
mi_lista= [5, 4, 8, 0, 7]
#          0  1  2
print(mi_lista[1])
print(mi_lista[-2])
print(mi_lista[2:4])
#propiedades:
# 1 son ordenadas: puedo acceder a cada elemento por su indice 

mi_lista[1]= True
print(mi_lista) # muestra toda la lista 

# 2 - son mutables: puedo modificar los elementos que contiene y la cantidad
# 3 - son Heterogeneas: soportan cualquier tipo de dato, incluso otras colecciones