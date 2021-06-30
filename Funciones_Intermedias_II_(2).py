##EJERCICIO_01: Actualiza los valores en diccionarios y listas
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