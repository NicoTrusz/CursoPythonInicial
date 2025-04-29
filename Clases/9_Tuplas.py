# Tuplas
# sintaxis
# 1- son heterogeneas
# 2- son ordenadas
# 3- SON INMUTABLES!!! 
mi_tupla = (True, 3.14, "hola")
print(mi_tupla[1])

#print(mi_tupla.count("hola")) # cantidad count
#print(mi_tupla.index("hola")) # posicion index

print(mi_tupla)
mi_tupla= list(mi_tupla) # comvierto mi tupla en una lista
mi_tupla[2] = "chau"
print(mi_tupla)