print("EJERCICIO_01: Actualiza los valores en diccionarios y listas")
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20}, {'a': 5,'x': 20, 'y': 21} ]
#
# 1.- Cambia el valor 10 en x a 15. Una vez que haya terminado,
#     x ahora debería ser [[5,2,3], [15,8,9]].
print("\n1.- Cambia el valor 10 en x a 15.")
print(f"Lista Original: {x}")
for i in range (0, len(x)):
    # print(x[i])
    for j in range (0, len(x[i])):
        # print (x[i][j])
        if x[i][j] == 10:
            x[i][j] = 15
            # print(f"El nuevo j: {x[i][j]}")
print (f"La lista modificada es: {x}\n")
#
# 2.- Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
print ("\n2.- Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'")
print (f"El diccionario original es: {students}")
for i in range (0, len(students)):
    if students[i]["last_name"] == 'Jordan':
        students[i]["last_name"] = 'Bryant'
print (f"El diccionario despuEs del cambio es: {students}\n")
#
# 3.- En el directorio sports_directory, cambia 'Messi' a 'Andres'
print ("\n3.- Cambiar 'Messi' a 'Andres' en el directorio sports_directory")
print (f"El directorio original es: {sports_directory}")
for deporte in sports_directory:
    #print (deporte)
    #print (sports_directory[deporte])
    for i in range (0, len(sports_directory[deporte])):
        if sports_directory[deporte][i] == 'Messi':
            sports_directory[deporte][i] ='Andres'
print (f"El directorio despuEs del cambio es: {sports_directory}.\n")
#
# 4.- Cambia el valor 20 en z a 30
print ("\n4.- Cambia el valor 20 en z a 30") ##  z = [ {'x': 10, 'y': 20}, {'a': 5,'x': 17, 'y': 21} ]
print (f"El z original es: {z}")
keymod = ''
valmod = 0
for i in range (0, len(z)):
    #print (z[i])
    temp = list(z[i].items())
    #print (temp)
    for m in range (0, len(temp)):
        #print (temp[m])
        for k in range (0, len(temp[m])):
            #print (temp[m][k])
            if temp[m][k] == 20:
                keymod = temp[m][k - 1]
                valmod = temp[m][k]
                #print (f"El Key a modificar es {keymod}")   #print (f"El Valor a modificar es {valmod}")
                z[i][keymod] = 30
                #print (z[i])
#print("Saliendo")
print(f"El nuevo z con el valor modificado es: {z}.\n")
#
print("#"*111, "\n")
#
print("EJERCICIO_02: Itera a travEs de una lista de diccionarios\n")
# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios,
# la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado.
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
#
def iteratedictionary(list_to_work2):
    for i in range (0, len(list_to_work2)):
        #print (z[i])
        temp2 = list(list_to_work2[i].items())
        #print (temp)
        for m in range (0, len(temp2)):
            #print (temp[m])
            for k in range (0, len(temp2[m])):
                #print (temp[m][k])
                print(f"{temp2[m][k]} - {temp2[m][k+1]}, {temp2[m+1][k]} - {temp2[m+1][k+1]}")
                break
            break
#
iteratedictionary(students)
#
print("#"*111, "\n")
#
print("EJERCICIO_03: ObtEn valores de una lista de diccionarios\n")
# Crea una función iteratedictionary2(key_name, some_list) que, dada una lista de diccionarios y un nombre de clave,
# la función imprima el valor almacenado en esa clave para cada diccionario.
#
def iteratedictionary2(key_name_3, list_to_work3):
    for i in range (0, len(list_to_work3)):
        temp3 = list(list_to_work3[i].items())
        #print (temp)
        for m in range (0, len(temp3)):
            #print (temp3[m])
            for k in range (0, len(temp3[m])):
                #print (temp3[m][k])
                if temp3[m][k] == key_name_3:
                    print(temp3[m][k+1])
                    break
#
iteratedictionary2('first_name', students)
print("\n")
iteratedictionary2('last_name', students)
#
print("#"*111, "\n")
#
print("EJERCICIO_04: Itera a travEs de un diccionario con valores de listas")
# Crea una función printInfo(some_dict) que, dado un diccionario cuyos valores son todas listas,
# imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados
# dentro de la lista de cada clave.
#
dojo = {
   'LOCATIONS': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'INSTRUCTORS': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#
def printinfo(some_dict_4):
    for clave, valores in some_dict_4.items():
        print(f"{len(valores)}  {clave}")
        for valor in valores:
            print(valor)
        print("\n")
#
printinfo(dojo)