# =======================================================================================
# El archivo se puede correr de principio a fin...
# ... dando el resultado de los cinco Ejercicios.
# =======================================================================================
# 1.- Cuenta regresiva :
# crea una función que acepte un número como entrada.
# Devuelve una nueva lista que cuenta hacia atrás en uno,
# desde el número (como el elemento 0) hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
###
print("EJERCICIO 01")
###
num_entrada = 17    ## Numero entrada para la función
def numtolist (num_ent):
    lista_salida = []
    for x in range(num_ent,0-1,-1):
        lista_salida.append(x)
    return lista_salida
print (numtolist(num_entrada))
# =======================================================================================
# 2.- Imprimir y volver:
# crea una función que recibirá una lista con dos números. 
# Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
###
print("EJERCICIO 02")
###
lista2 = [17,19]
def prnt_rtrn2 (list_to_work2):
    print ("El primer valor es: " , lista2[0])
    return lista2[1]
x2 = prnt_rtrn2(lista2)
print("El return (segundo valor) es: " , x2) 
# =======================================================================================
# 3.- First Plus Length :
# crea una función que acepta una lista y devuelve 
# la suma del primer valor de la lista más la longitud de la lista.
#  Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
###
print("EJERCICIO 03")
###
lista3 = [7,2,3,4,7,0,11,15,23,-56]
def first_plus_length(list_to_work3):
    return lista3[0] + len(lista3)
print ("El resultado de Primero mas Longitud es: " , first_plus_length(lista3))
# =======================================================================================
# 4.- Valores mayores que el segundo:
# escribe una función que acepte una lista y crea una nueva lista que contenga 
# solo los valores de la lista original que sean mayores que su segundo valor.
# Imprima cuántos valores son y luego devuelva la nueva lista.
# Si la lista tiene menos de 2 elementos, haga que la función devuelva False
#  Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 
#           y devolver [5,3,4]
#  Ejemplo: values_greater_than_second ([3]) debería devolver False
###
print("EJERCICIO 04")
###
lista4 = [7,9,31,4,7,10,11,5,23,-5]
new_lista4 = []
def values_greater_than_second (list_to_work4):
    if len(lista4) < 2:
        print("false")
    else:
        for val in lista4:
            if val > lista4[1]:
                new_lista4.append(val)
        print(f"La cantidad de valores mayores que el segundo de la lista ({lista4[1]}) son: " , len(new_lista4))
        return new_lista4 
print("El return de la funciOn es la nueva lista, la cual es: " , values_greater_than_second(lista4))
# =======================================================================================
# Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros:
#   tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual
#   al tamaño dado y cuyos valores son todos los valores dados.
#  Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#  Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
###
print("EJERCICIO 05")
###
tamanho_y_valor5 = (7,17)
lista_salida5 = []
def length_and_value5(tupla_tamanho_y_valor5):
    for i in range (0 , tamanho_y_valor5[0] , 1):
        lista_salida5.append(tamanho_y_valor5[1])
    return (lista_salida5)
print("El resultado es la siguiente lista: " , length_and_value5(tamanho_y_valor5))
# =======================================================================================
# jemm
# ==============================E.N.D.===================================================