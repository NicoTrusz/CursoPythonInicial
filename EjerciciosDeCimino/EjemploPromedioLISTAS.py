# calculo promedios y muestro nros ingresados
cant_nros = input("Ingrese cantidad: ")
acumulador = [] # lista vacia

for n in range(int (cant_nros)) :
    valor = input("ingrese valor: ")
    acumulador.append(float(valor)) # .append agrega elementos a la lista al final /// .append(str(valor)) puedo agregar a mi lista cadenas
    print(acumulador)
    print(len(acumulador)) # len muestra cantidad de elementos en mi lista

promedio= sum(acumulador) / int(cant_nros) # o len(acumulador)
print(f"el promedio es: {promedio}")
print(f"los valores ingresados: {acumulador} ")
#print(acumulador,type(acumulador))

# Lista de nombres, pido un ingreso y verifico que este registrado

nombres = ['cristian','naranjo','leia']
ingreso= input("Ingrese nombre: ")

# puedo evaluar la pertenencia
if ingreso in nombres:
    print("pertenece")
else:
    # nombres.insert(0, ingreso) en el caso de querer agregar en una pocicion especifica
    print("no pertenece")

# nombres.pop() elimina el ultimo elemento
# nombres.pop(3) elimina el elemento en la posicion 3
# del nombre[3] elimino el elemento en la posicion 3 y es obligatorio colocar la posicion "slicing"
# mis_nros.index() #devuelve el indice de la 1ra ocurrencia
# mis_nros.count() # devuelve la cantidad de ocurrencias
# mis_nros.sort() # ordeno de menos a mayor
# mis_numeros.sort(reverse=True) # ordena de mayor a menor