from random import*
from time import time


def combsort(num):
    # Inicializar brecha
    gap = len(num)
    # Inicializar intercambiado como verdadero para asegurarse de que
    # ejecuciones de bucle
    swaps = True
    # Sigue corriendo mientras la brecha sea mayor a 1 o
    # la ultima iteración provocó un cambio
    while gap > 1 or swaps:
        #Encontar la siguiente brecha
        gap = max(1, int(gap / 1.25))  
        swaps = False
        for i in range(len(num) - gap):
            j = i+gap
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
                swaps = True
# Generacion de arreglos
def genArr(num, op):
	if(op=="N"): # Arreglo aleatorio normal
		arr = [randint(0,99999) for x in range(num)]
	elif(op=="A"): # Arreglo aleatorio ascendente
		arr = genArr(num, 'N')
		combsort(arr)
	elif(op=="D"): # Arreglo aleatorio descendente
		arr = genArr(num, 'N')
		combsort(arr)
		arr.reverse()
	else:
		print("Opcion no valida...")
	return arr


#Main
# Caso Promedio
arrCasoP = genArr(10000, 'N')
start_time1 = time() #Inicio
combsort(arrCasoP)
elapsed_time1= time() - start_time1 #Fin
print("\nTiempo para el caso promedio: ", elapsed_time1) #Muestra el tiempo transcurrido

# Mejor caso: Arreglo en orden ascendente
arrMCaso = genArr(10000, 'A')
start_time2 = time() #Inicio
combsort(arrMCaso)
elapsed_time2 = time() - start_time2 #Fin
print("\nTiempo para el mejor caso: ", elapsed_time2) #Muestra el tiempo transcurrido


# Peor caso: Arreglo en orden descendente
arrPCaso = genArr(10000, 'D')
start_time3 = time() #Inicio
combsort(arrPCaso)
elapsed_time3 = time() - start_time3 #Fin
print("\nTiempo para el peor caso: ", elapsed_time3) #Muestra el tiempo transcurrido

