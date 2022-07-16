from random import*
from time import time

# Algoritmo SelectionSort        
def selectionSort(arr):
    tam = len(arr)
    # i indica cuántos elementos se ordenaron
    for i in range(tam):
        # Para encontrar el valor mínimo del segmento sin clasificar
        # Asumimos que el primer elemento es el más bajo
        min_index = i
        # Luego usamos j para recorrer los elementos restantes
        for j in range(i+1, tam):
            # Actualizamos min_index si el elemento en j es menor que él
            if arr[j] < arr[min_index]:
                min_index = j
        # Después de encontrar el elemento más bajo de las regiones sin clasificar
        # cámbielo por el primer elemento sin clasificar
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Generacion de arreglos
def genArr(num, op):
	if(op=="N"): # Arreglo aleatorio normal
		arr = [randint(0,99999) for x in range(num)]
	elif(op=="A"): # Arreglo aleatorio ascendente
		arr = genArr(num, 'N')
		selectionSort(arr)
	elif(op=="D"): # Arreglo aleatorio descendente
		arr = genArr(num, 'N')
		selectionSort(arr)
		arr.reverse()
	else:
		print("Opcion no valida...")
	return arr


#Main
# Caso Promedio
arrCasoP = genArr(1000, 'N')
start_time1 = time() #Inicio
selectionSort(arrCasoP)
elapsed_time1= time() - start_time1 #Fin
print("\nTiempo para el caso promedio: ", elapsed_time1) #Muestra el tiempo transcurrido


# Mejor caso: Arreglo en orden ascendente
arrMCaso = genArr(1000, 'A')
start_time2 = time() #Inicio
selectionSort(arrMCaso)
elapsed_time2 = time() - start_time2 #Fin
print("\nTiempo para el mejor caso: ", elapsed_time2) #Muestra el tiempo transcurrido


# Peor caso: Arreglo en orden descendente
arrPCaso = genArr(1000, 'D')
start_time3 = time() #Inicio
selectionSort(arrPCaso)
elapsed_time3 = time() - start_time3 #Fin
print("\nTiempo para el peor caso: ", elapsed_time3) #Muestra el tiempo transcurrido


