def entrada():
    array = [] #declaracion arreglo
    leng = int(input("Tamaño del vector: ")) #entrada tamaño del arreglo
    for i in range(leng): 
        datum = int(input("Numero {}:".format(i+1))) #entrada de los datos que conforman el arreglo
        array.append(datum) #agregarlo a la lista
    array_revers = array    #asiganr mismo valor a otro arreglo
    array_revers = revers(array) #llamada metodo
    print (array) #imprimir arreglo 1
    print (array_revers) # imprimir arreglo invertido
    print ("------------------------") 
    count_Int (array) #llamda de metodo
    print ("------------------------")
    print ("El 0 se encuentra en la posicion "+str(index_0 (array))+" del primer arreglo") #imprimir posicion del 0
    print ("El 0 se encuentra en la posicion "+str(index_0 (array_revers))+" del segundo arreglo") #imprimir posicion del 0
    

def revers (array): #metodo
    
    if array == []:
        return array
    else:
        return [array[-1]] + revers(array[:-1]) #recursividad para invertir lista

def count_Int (array): #metodo
     
    counterP = 0 #Contador
    counterN = 0 #Contador
    for i in array:
        if (i > 0):
            counterP += 1 #conteo de numeros enteros
        elif (i < 0):
            counterN += 1  #conteo de numeros negativos
 
    print("el arreglo tiene:\n{} entero\n{} negativo".format(counterP,counterN)) #impresion de los resultados

def index_0 (array):
    return array.index(0) #buscar el valor 0

entrada() #llamada de metodo