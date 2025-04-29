# Operadores de asignacion 
# =

# Definir Var_1 como Entero 

#Python es de tipeado dinamico

var_1 = 5 
var_2 = 3.14 
var_3 = "Comision 23593"
print("var_1 vale: ", var_1)
print(type(var_1)) # tipo de variable >> (type())
print("var_1 vale: ", var_2)
print(type(var_2)) # tipo de variable >> (type())
print("var_1 vale: ", var_3)
print(type(var_3)) # tipo de variable >> (type())

# Control de flujo
# Condicionales
# Si <condicion> entonces
#   <ejecucion por cerdadero>
# FinSi
print("primer programa")
print("\n****inicio****\n")
edad= 48
if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")
# la estructura se cierra al salir del indentado (tabulacion)
print("\n****Fin****\n")

# Entrada de datos (porr consola)
# edad = 18
print("Segundo programa\n")
print("Inicio\n")
edad_1= input("ingrese edad: ") #DEVUELVE DATOS DEL TIPO STR (imput())
print(edad_1,type(edad_1)) # tipo de variable >> (type())
edad_1= int (edad_1)
print(edad_1,type(edad_1)) # tipo de variable >> (type())
print("\nFin\n")

# suma dos enteros 
valor_1= input("ingrese valor1:")
valor_1= int(valor_1)
print("\n")
valor_2= input("ingrese valor2:")
valor_2= int(valor_2)
print("la suma es: ", valor_1+ valor_2) #forma corta print("la suma es: ", int(valor_1)+int(valor_2))
