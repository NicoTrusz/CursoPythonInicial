mi_bbdd =[
    ["cristian", 42, False], # 0  # 0 1 2
    ["leia",4,True],         # 1  # 0 " "
    ["naranjo",7.5,True],    # 2  # 0 " "
]
ingreso = input("Ingrese nombre: ")

for fila in mi_bbdd:
    #print(fila)
    if ingreso in fila:
        print(f'''
        Nombre: {fila[0]}
        Edad:   {fila[1]}
        Felino: {fila[2]}
            ''')
        break
else:
    print("no existe")