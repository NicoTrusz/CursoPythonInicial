# como calcular raiz cuadrada sin libreria

print(4 ** 2)
print(4 ** (1/2))
print((-4) ** (1/2))

# Funciones incorporadas con el interprete y propias
# incorporadas o built-in
# https://docs.pýthon.org/es/3/library/functions.html

# Funciones propias
# 1. Fundamento: encapsular codigo repetido y modularizar un algoritmo
# 2. Tiempos de la funcion: definicion e invocacion 

def sumar_5_3():
    print(f"la suma de 5 y 3 = {5 +3}")

print("algunas lineas de codigo")
print("*"*50)
sumar_5_3()

#print(f"la suma de 5 y 3 = {5 +3}")
#print("mas lineas de codigo")
#print(f"la suma de 5 y 3 = {5 +3}")
#print("mas lineas de codigo")
#print(f"la suma de 5 y 3 = {5 +3}")

#print(f"la suma de 5 y 4 = {5 + 4}")

def sumar_dos_numeros(num_1 , num_2):
    print(f"la suma de {num_1} y {num_2} = {num_1 + num_2}")
print("*"*50)
sumar_dos_numeros(5, 3) # invocacion con argumentos por posicion
print("*"*50)
sumar_dos_numeros(5, 4)
# Sumar_dos_numeros(5) #espera dos argumentos

# IMPORTANTE NUNCA COLOCAR UNA VARIABLE GLOBAL DENTRO DE UNA FUNCION SINO PASARLA POR PARAMETRO NUNCA LLAMAR UNA VARAIBLE GLOBAL DENTRO DE LA FUNCION