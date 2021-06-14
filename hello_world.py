# 1. TAREA: imprimir "Hola mundo"
print( "Hola mundo" )
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Juan Enrique"
print( "Hola" , name )	# con una coma
print( "Hola   " + name )	# con un +
print(f"Hola {name} Malaver")	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
name = 42
print( "Hola" , name , "!" )	# con una coma
#BORRAR(da el error esperado)# print( "Hola" + name + "!" )	# con un + - !Este debería darnos un error!
print( "Hola" + str(name) + "!" + "(solucionando el error con str()" )   # Soluciones al error de arriba
print( "Hola " + str(name) + " ! " + " (solucionando el error con str()" ) # haciendo el número un string
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "op_1:  Me encanta comer {} and {}.".format(fave_food1, fave_food2) ) # con .format()
print( "bonus:  Me encanta comer {1} and {0}.".format(fave_food1, fave_food2) ) # con .format()
print(f"op_2:  Me encanta comer {fave_food1} and {fave_food2}.") # con una cadena f