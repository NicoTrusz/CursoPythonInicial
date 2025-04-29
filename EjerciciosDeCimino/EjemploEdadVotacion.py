# edades votacion 
# edad < 16 //edad <= 17 or edad > 70 // edad
''' Algoritmo edad_votacion
    // < 16: no puedo votar
    // 16 y 17: no obligatorio
    // 18 a 70: obligatorio
    // 70 : no obligatorio
    '''
print("Inicio\n")
edad =input("ingrese edad:")
edad= int(edad)
if edad <0 or edad >122:
    print("Ingreso de edad incorrecto")
elif edad< 16 : # Opcion 1
    print("no podes votar")
elif edad <= 17 or edad > 70: # Opcion 2
    print("podes votar no es obligacion")
else: # Opcion 3 si las anterires son falsas 
    print("es obligatorio votar")
print("Fin")