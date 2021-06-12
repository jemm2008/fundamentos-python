# Crea un archivo de Python llamado for_loop_basic1.py que realice las siguientes tareas.
#===========================================================================================================================
# .-01_Básico : imprime todos los enteros del 0 al 150.
for x in range (0, 151,1):
    print (x)
#===========================================================================================================================
# Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range (5, 5005,5):
    print (x)
#============================================================================================================================
# Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. 
# Si es divisible por 10, imprima "Coding Dojo".
for x in range (1,31,1):
        if x%10==0:
            print ("Coding Dojo")
        else:
            if x%5==0:
                print ("Coding")
            else:
                print(x)
#==============================================================================================================================
# ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
num=0
for x in range (1,500000,2):
    # print(x)
    num=num+x
print(num)
#================================================================================================================================
# Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for x in range (2018,0,-4):
    print(x)
#=================================================================================================================================
# Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, 
# el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum=2
highNum=9
mult=3
for x in range (lowNum,highNum+1):
    if x%3==0:
        print(x)
#======================================================E.N.D.======================================================================