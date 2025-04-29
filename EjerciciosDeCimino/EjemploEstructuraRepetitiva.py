# Defino clave y pido ingreso, si no coincide repito pedido
clave ="123abc"
ingreso = ""
intentos = 0
# estructura repetitiva
while intentos < 3:
    ingreso = input("ingrese clave: ")
    if ingreso == "otra oportunidad": # posible forma de romper el codigo 
        print("este ingreso no consume intentos")
        continue # vuelve al inicio del bucle y no consume intentos 
    elif clave == ingreso:
        print("ingreso exitoso!")
        break # rompo bucle
    intentos += 1
else:
    print("usuario bloqueado!")

#if clave == ingreso:
#    print("ingreso exitoso")
#else:
#    print("ususario bloqueado")