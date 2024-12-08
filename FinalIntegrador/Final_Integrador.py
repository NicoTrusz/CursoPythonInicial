# crear usuario (nombre y contraseña) //if de ususario repetido LISTO
# iniciar sesion (nombre y contraseña) // mostrar intentos      LISTO
# for o while de 3 intentos                                     LISTO
# salir del programa                                            LISTO
# almacenar archivo de usuarios (archibo txt y formato JSON)

#*********************************************************************************************************************#

# aun me falta fijarme si armar funciones o definiciones para cada operacion (crear, iniciar y usuario repetido) y llamarlas desde las opciones 1 o 2 20/11/23 LISTO 23/11/23
# averiguar como limpiar terminal entre cada operacion para mayor proligidad 20/11/23

#*********************************************************************************************************************#
import os
import json

#************CREAR USUARIO**************#
def crear_usuario(usuario, contraseña, dic):
    if usuario in dic:
        print("el usuario ya existe")
    else:
        dic[usuario] = contraseña
        print("Usuario creado exitosamente!")

#************INICIAR SESION*************#
def iniciar_sesion(usuario_1):
    for intentos in range(3):
        print("*" * 30)
        print("Opción >>> 2")
        usuario = input("ingrese usuario: ") .lower()
        contraseña = input("ingrese contraseña: ").lower()
        if usuario in usuario_1 and usuario_1[usuario] == contraseña :  #leer usuario contraseña y comparar con los datos de mi o mis listas para definir usuario exitoso o bloqueo despues de 3 intentos
            print("Ingreso Exitoso!")
            break
        elif intentos < 2 :
            print(f"vuelva a intentarlo: intentos--> {intentos +1}")
        else :
            print(f''' intentos--> {intentos +1}\nUsuario BLOQUEADO''')

# REVISAR URGENTE NO ME ESTA RELACIONANDO USUARIO CON CONTRASEÑA POR ENDE SE ME DIFICULTA ESTA OPCION LO UE ESTA HACIENDO ES VER QUE EL DATO EXISTA EN TODO EL VECTOR O CADENA 23/11/23#
# SOLUCIONADO CON DICCIONARIO POR LA RELACION CLAVE VALOR 23/11/23 #

#********** LISTA DE USUARIOS ********#
def lista_usuarios(usuarios):
    usuario= input("ingrese usuario: ")
    contraseña= input("ingrese contraseña: ")
    if usuario == "ADMIN" and contraseña == "ADMIN" :
        print("*"*30)
        for clave in usuarios.keys():
            print(f"Usuario: {clave} - Contraseña: {usuarios[clave]}") 
    else :
        print("USTED NO ES ADMIN DEL PROGRAMA")


#************** SALIR *****************#
#**** Y GUARDO EN TXT O JSON **********#
def salir(nombre_archivo, formato, dic):
    with open(nombre_archivo, "w") as archivo:
        if formato == "txt":
            for nombreusuario ,contraseña in dic.items():
                archivo.write(f"{nombreusuario}: {contraseña}\n")
        elif formato == "json":
            json.dump(dic, archivo, indent=4)


#************ VARIABLES ***************#
usuarios = {}

#************** MENU ******************#
while True : # coloque un valor absurdo para poder ingresar en el bucle While y poder repetir la creacion de usuarios o el ingreso. Y rompo el bucle con la opcion 3 salir con break
    print("*" * 30)
    os.system("cls")
    opcion= input("***menu***\n1_Crear Usuario\n2_Iniciar sesion\n3_Salir\n4_listado de usuarios\nsu opcion es: ")
    #opcion= int(opcion) descubri error si por accidente tipeas cualquier tipo STR rompia el codigo 21/11/23
    if opcion == "1": # crear usuario
        print("*" * 30)
        print("Opción >>> 1")
        n_usuario= input("Ingrese usuario: ").lower()
        n_contraseña= input("Ingrese Contraseña: ").lower()
        crear_usuario(n_usuario, n_contraseña, usuarios)


    elif opcion == "2": # iniciar sesion
        iniciar_sesion(usuarios)

    elif opcion == "3": # salir
        tipo_formato = input("ingrese el formato (txt o json): ").lower()
        salir("BaseDeDatos." + tipo_formato, tipo_formato, usuarios)
        print("*" * 30)
        print("Opción >>> 3")
        print(''' Gracias por utilizar nuestra app 
            Fin de programa''' )
        break
    
    elif opcion == "4": # lista de usuarios y contraseñas
        lista_usuarios(usuarios)

    else: # la opcion no es correcta 
        print("*" * 30)
        print("la opcion no coincide con ninguna ")