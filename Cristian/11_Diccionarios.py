# Diccionarios
# Palabra: definicion 
# pares clave: valor   //  key: value
# Sintaxis

numeros = {} # diccionario vacio
numeros= {"uno": 1,
          "dos": 2.0, 
          "tres": [1, 2, 3], 
          "dato bool": 7 > 5
 }
print(numeros)
print(numeros["uno"])
numeros["uno"] = (4,5,7) # forma rellenar un dicc // nick_dicc[clave] = valor
print(numeros)
# propiedades
# 1- Heterogeneos: 
#           valor: soportan cualuier tipo de dato
#           clave: dato inmutable -> cadenas / tuplas / numeros
# 2- NO SON ORDENADOS, no tienen indices
# 3- Mutabilidad: son mutables

# Inmutabilidad numerica

num_1 = 5
print(num_1 * 2 )

num_1 = num_1 * 2
print(num_1)

# Diccionario ---> JSON = JavaScript Objet Notation
# https://jsonplaceholder.typicode.com/

# A partir de Pyton 3.7 los dict() "se pueden ordenar"
# https://www.w3schools.com/python/python_ref_dictionary.asp
# https://docs.python.org/3/tutorial/datastructures.html

mi_dicc= {
    "comision": 23593,
    "dias": ["lunes", "miercoles"],
    "horario": "de 10:00 a 11: 30"
}

print(mi_dicc.keys()) # devuelve las claves fomat lista
print(mi_dicc.values()) # devuelve las variables format lista
print(mi_dicc.items()) # devuelve el diccionario en formt tuplas