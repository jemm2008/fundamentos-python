# =======================================================================================
# 1.- TAMAÑO GRANDE: 
# dada una lista, escriba una función que cambie 
# todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores 
# son ahora [-1, "big", "big", -5]
###
print("EJERCICIO 01")
###
lista1 = [-1, 7, 11, -2, 15, -5]
def tam_gde1(list_to_work1):
    lista_salida1 = []
    for elemento in lista1:
        if elemento < 0:
            lista_salida1.append(elemento)
        else:
            lista_salida1.append("big")
    return (lista_salida1)
print(f"El resultado con la lista {lista1} es: {tam_gde1(lista1)}.")
# =======================================================================================
# 2.- CONTAR POSITIVOS: 
# dada una lista de números, cree una función para reemplazar el último valor 
# con el número de valores positivos. (Tenga en cuenta que cero no se considera
# un número positivo).
# Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
# Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve
###
print("EJERCICIO 02")
###
lista2 = [-1, 1, -2, 1, -5, 0, 9]
def contar_positivos(list_to_work2):
    valores_positivos2 = 0
    lista_final2 = lista2
    for elemento in lista_final2:
        if elemento > 0:
            valores_positivos2 +=1
    lista_final2.pop()
    lista_final2.append(valores_positivos2)
    return (lista_final2)
print (f"la lista original es: {lista2}; y la nueva lista es: {contar_positivos(lista2)}")
# =======================================================================================
# 3.- SUMA TOTAL: 
# crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7
###
print("EJERCICIO 03")
###
lista3 = [1, 5, 3, 3, -7, 11, 7]
def suma_total3(list_to_work3):
    sumtotal3 = 0
    for elemento in lista3:
        sumtotal3 += elemento
    return (sumtotal3) 
print(f"la lista original es: {lista3}; y la suma de sus elementos es: {suma_total3(lista3)}.")
# =======================================================================================
# 4.- PROMEDIO: 
# crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
###
print("EJERCICIO 04")
###
lista4 = [1, 5, 4, 3, 0]
def promedio4(list_to_work4):
    sumatoria_promedio4 = 0
    for elemento in lista4:
        sumatoria_promedio4 += elemento
    sumatoria_promedio4 = sumatoria_promedio4 / len(lista4)
    return (sumatoria_promedio4)
print(f"La lista original es: {lista4}; y el promedio de sus elementos es: {promedio4(lista4)}.")
# =======================================================================================
# 5.- LONGITUD: 
# crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0
###
print("EJERCICIO 05")
###
lista5 = [37,2,1, -9, 3, 2, 11]
def longitud5(lis_to_work5):
    long_5 = len(lista5)
    return (long_5)
print (f"la longitud de la lista {lista5} es: {longitud5(lista5)}")
# =======================================================================================
# 6.- MINIMO: 
# crea una función que tome una lista de números y devuelva el valor mínimo en la lista. 
# Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False
###
print("EJERCICIO 06")
###
lista6 = [7, 1, -11, 0, -10] #[3] #[]    ## Funciona en los tres casos   
def minimo6(lis_to_work6):
    if len(lista6) == 0:   
        return False
    if len(lista6) == 1:
        return lista6[0]
    if len(lista6) > 1:
        minim_6 = lista6[0]
        for x in range(1,len(lista6),1):
            if lista6[x] < minim_6:
                minim_6 = lista6[x]
        return minim_6
print(f"La Lista inicial es: {lista6}; y su elemento de menor valor es: {minimo6(lista6)}")
# =======================================================================================
# 7.- MAXIMO: 
# crea una función que toma una lista y devuelve el valor máximo en ella.
# Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False
###
print("EJERCICIO 07")
###
lista7 = [-7, 1, -11, 17, -10, 12]     # [7]   # []     ## Funciona en los tres casos   
def maximo7(list_to_work7):
    if len(lista7) == 0:   
        return False
    if len(lista7) == 1:
        return lista7[0]
    if len(lista7) > 1:
        maxim_7 = lista7[0]
        for x in range(1,len(lista7),1):
            if lista7[x] > maxim_7:
                maxim_7 = lista7[x]
        return maxim_7
print(f"La Lista inicial es: {lista7}; y su elemento de mayor valor es: {maximo7(lista7)}")
# =======================================================================================
# 8.- ANALISIS FINAL:
# crea una función que tome una lista y devuelva un diccionario que tenga
# la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver 
# {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}
###
print("EJERCICIO 08")
###
lista8 = [37,2,1, -9]
def analisis_final8(list_to_work8):
    total8 = 0
    minimo8 = lista8[0]
    maximo8 = lista8[0]
    for elemento in lista8:
        total8 += elemento
        if elemento < minimo8:
            minimo8 = elemento
        if elemento > maximo8:
            maximo8 = elemento
    return dict(total = total8, promedio = total8 / len(lista8), minimo = minimo8, maximo = maximo8, longitud = len(lista8))
print(f"El resultado del AnAlisis Final a la lista {lista8} es:") 
print(analisis_final8(lista8))
# =======================================================================================
# 9.- LISTA INVERSA:
# crea una función que tome una lista y la devuelva con los valores invertidos.
# Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante
# las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
###
print("EJERCICIO 09")
###
lista9 = [37, 2, 5, 1, -9]
print(f"La lista original antes de la inversiOn es: {lista9}")
def lista_inversa9(list_to_work9):
    for x in range(0, int(len(lista9) / 2), 1):
        lista9[x],lista9[len(lista9) - 1 - x] = lista9[len(lista9) - 1 - x],lista9[x]
    return lista9
print(f"La lista invertida es: {lista_inversa9(lista9)}")
