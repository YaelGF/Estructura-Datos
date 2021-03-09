import numpy as np #importamos numpy
import random #libreria para elegir al ganador
class Arreglos: #creamos una clase 
    array1 = []
    array2 = []
    diagonal = []
    invetido = []
    def _init_(self): #agregamos el constructor
        pass

    def crear_arreglos(self): #creamos un error
        try: #intente hace todo lo de adentro (si hay errores)
            for i in range(2): #de la vuelta dos veces para las dos matrices
                print("\nGrupo "+str(i+1)+":") #indique el grupo
                filas = int(input("Ingresa no. filas: ")) #pedimos filas y columnas que ingrese el usuario
                columnas = int(input("Ingresa no. columnas: "))
                for j in range(filas): #que recorra las filas
                    if i == 0: #si está en la posición 0 almacena array1
                        self.array1.append([])
                    else: #caso contrario en el 2
                        self.array2.append([])
                    print("Fila "+str(j+1)+":") #nos imprima el no. de fila que va recorriendo
                    for k in range(columnas): #que recorra las columnas
                        lista = int(input("Ingresa elemento para columna "+str(k+1)+": ")) #aquí vamos preguntando los valores que va a almacenar
                        if i == 0: #si es posición 0 almacena array1
                            self.array1[j].append(lista)
                        else: #caso contrario en el 2
                            self.array2[j].append(lista)
            self.array1 = np.array(self.array1) #convetimos el array a uno mismo pero con las propiedades de NUmpy, lo mismo el 2
            self.array2 = np.array(self.array2)
            print("\nAcomodo del grupo 1: \n",self.array1) #imprimimos ambas matrices
            print("Acomodo del grupo 2: \n",self.array2)
        except: #si hay algún error imprima un mensja y vuelva a ejecutar el método
            print("Datos incorrectos, intente de nuevo.")
            return self.crear_arreglos()

    def eliminar(self): #método para eliminar alguna columna
        try:
            arreglo = int(input("Ingrese grupo (1 o 2) para eliminar columna: ")) #preguntamos cuál matriz
            
            if arreglo == 1: #si es igual a 1 es la matriz 1
                tamaño1 = self.array1.shape #obtenemos las dimensiones
                columnas = int(input("Ahora ingresa el no. columna (hay "+str(tamaño1[1])+"): ")) #pedimos la posición
                self.array1 = np.delete(self.array1, columnas, axis = 1) #con delete reciebiendo como parametro el nombre del array, la posición y axis igual a 1 que indica que va a eliminar una columna
                print("\nNuevo acomodo: \n",self.array1) #imprimimos nuevo valor de la matriz

            elif arreglo == 2: #si es igual a 2 es la matriz 2
                tamaño2 = self.array2.shape #obtenemos las dimensiones
                columnas = int(input("Ahora ingresa el no. columna (hay "+str(tamaño2[1])+"): ")) #pedimos la posición
                self.array2 = np.delete(self.array2, columnas, axis = 1) #con delete reciebiendo como parametro el nombre del array, la posición y axis igual a 1 que indica que va a eliminar una columna
                print("\nNuevo acomodo: \n",self.array2) #imprimimos nuevo valor de la matriz
            else: #si no es ni 1 ni 2 mande un mensaje y repita el método
                print("Datos incorrectos, intente de nuevo.")
                return self.eliminar()
        except: #si ingresó la columna fuera de rango o diferente tipo de dato lo muestre y ejecute el método de nuevo
            print("Columna incorrecta, intente de nuevo.")
            return self.eliminar()

    def agregar(self): #metodo agregar fila columna en cualquier matriz
        try:
            tamaño1 = self.array1.shape #obtenemos las dimensiones
            tamaño2 = self.array2.shape
            arreglo = int(input("Ingrese grupo (1 o 2) para agregar elemento: ")) #preguntamos cuál matriz
            
            if arreglo == 1: #si es igual a 1 es la matriz 1
                elegir = input("¿Deseas ingresar fila o columna? ").lower() #preguntamos si fila o columna
                if elegir == "fila": #si es fila
                    print("Al querer ingresar una fila tiene que ingresar una matriz con el mismo no. de columnas ("+str(tamaño1[1])+" elementos): ") #mostramos qué tiene que ingresar el usuario
                    row = []
                    for z in range (tamaño1[1]): #lo repetimos el no. de columnas que tenga esa matriz
                        elemento = int(input("Ingresa elemento "+str(z+1)+": ")) #pedimos los valores
                        row.append(elemento) #los almacenamos
                    valores = np.array(row) #usamos propiedades de Numpy
                    valores = valores.reshape(1,-1) #lo hacemos matriz leyendo una fila y que en automatico se ajuste el no. de columnas
                    self.array1 = np.append(self.array1, valores, axis =0) #con append recibiendo como parametros la matriz, los nuevos valores y la axis indicando fila

                elif elegir == "columna": #si es columna
                    print("Al querer ingresar una columna tiene que ingresar una matriz con el mismo no. de filas ("+str(tamaño1[0])+" elementos): ") #mostramos qué tiene que ingresar el usuario
                    row = []
                    for z in range (tamaño1[0]): #lo repetimos el no. de filas que tenga esa matriz
                        elemento = int(input("Ingresa elemento "+str(z+1)+": ")) #pedimos los valores
                        row.append(elemento) #los almacenamos
                    valores = np.array(row) #usamos propiedades de Numpy
                    valores = valores.reshape(-1,1) #lo hacemos matriz leyendo una columna y que en automatico se ajuste el no. de filas
                    self.array1 = np.append(self.array1, valores, axis =1) #con append recibiendo como parametros la matriz, los nuevos valores y la axis indicando columna
                else: #si escribe mal el usuario mande un mensaje y vuelva a ejecutar el método
                    print("Datos inccorrectos, favor de verificar.")

                print("\nNuevo acomodo: \n",self.array1) #nos muestra el nuevo resultado

            elif arreglo == 2: #mismo proceso que anterior, solo que con la matriz 2:
                elegir = input("¿Deseas ingresar fila o columna:").lower()
                if elegir == "fila":
                    print("Al querer ingresar una fila tiene que ingresar una matriz con el mismo no. de columnas ("+str(tamaño2[1])+" elementos): ")
                    row = []
                    for z in range (tamaño2[1]):
                        elemento = int(input("Ingresa elemento "+str(z+1)+": "))
                        row.append(elemento)
                    valores = np.array(row)
                    valores = valores.reshape(1,-1)
                    self.array2 = np.append(self.array2, valores, axis =0)

                elif elegir == "columna":
                    print("Al querer ingresar una columna tiene que ingresar una matriz con el mismo no. de filas ("+str(tamaño2[0])+" elementos): ")
                    row = []
                    for z in range (tamaño2[0]):
                        elemento = int(input("Ingresa elemento "+str(z+1)+": "))
                        row.append(elemento)
                    valores = np.array(row)
                    valores = valores.reshape(-1,1)
                    self.array2 = np.append(self.array2, valores, axis =1)
                else:
                    print("Datos inccorrectos, favor de verificar.")

                print("\nNuevo acomodo: \n",self.array2) #nos muestra el nuevo resultado

            else:
                print("Datos incorrectos, intente de nuevo.") #si ingreso el numero de matriz incorrecto
                return self.eliminar()

            repetir = input("¿Desea agregar más elementos? (SI/NO): ").lower() #preguntamos si desea almacenar más elementos
            if repetir == "si": #si es si vuelva a ejecutar todo el método
                return self.agregar()
        except: #si hay algún error mande y mensaje y retorne el método
            print("Datos erroneos, intente de nuevo.")
            return self.agregar()


    def sumar_multiplicar(self): #método sumar y multiplicar ambas matrices
        tamaño1 = self.array1.shape #obtenemos las dimensiones
        fila1 = tamaño1[0] #obtemos tamaño de fila de la matriz 1
        columna1 = tamaño1[1] #obtemos tamaño de columna de la matriz 1
        tamaño2 = self.array2.shape
        fila2 = tamaño2[0] #obtemos tamaño de fila de la matriz 2
        columna2 = tamaño2[1] #obtemos tamaño de columna de la matriz 2

        if fila1 == fila2 and columna1 == columna2: #hacemos varias validaciones, si ambas matrices son del mismo tamaño en automatico haga la suma y la multiplicación, así también imprimir
            suma = self.array1 + self.array2
            print("\nGrupos ajustados:  \n")
            print(self.array1,"\n", self.array2)
            print ("\nSuma de ambos grupos: \n",suma)
            multiplicacion = self.array1 * self.array2
            print ("Multiplicación de ambos grupos: \n",multiplicacion)

        elif fila1 == columna2 and fila2 == columna1: #si la fila de matriz 1 es igual a la columna de matriz 2 y la fila de matriz 2 es igual a la columna de matriz 1 solo invertimos las filas por columnas de la matriz 2, hacemos las operaciones e imprimimos
            self.array2 = self.array2.tranpose()
            print("\nGrupos ajustados: \n")
            print(self.array1,"\n",self.array2)
            suma = self.array1 + self.array2
            print ("\nSuma de ambos grupos: \n",suma)
            multiplicacion = self.array1 * self.array2
            print ("Multiplicación de ambos grupos: \n",multiplicacion)

        elif fila1 > fila2: #si la fila de la matriz 1 es mayor a la de 2
            self.array1 = np.delete(self.array1, -1, axis = 0) #eliminar la ultima fila de la matriz 1 
            return self.sumar_multiplicar() #vuelve a ejecutar el método
        elif columna1 > columna2: #si la columna de la matriz 1 es mayor a la de 2
            self.array1 = np.delete(self.array1, -1, axis = 1) #eliminar la ultima columna de la matriz 1 
            return self.sumar_multiplicar() #vuelve a ejecutar el método

        elif fila1 < fila2: #si la fila de la matriz 1 es menor a la de 2
            self.array2 = np.delete(self.array2, -1, axis = 0) #eliminar la ultima fila de la matriz 2
            return self.sumar_multiplicar() #vuelve a ejecutar el método
        elif columna1 < columna2: #si la columna de la matriz 1 es menor a la de 2
            self.array2 = np.delete(self.array2, -1, axis = 1) #eliminar la ultima columna de la matriz 2
            return self.sumar_multiplicar() #vuelve a ejecutar el método
        #seguirá el bucle hasta que cumpla la condición 1 o 2 del método

    def invertir(self): #metodo para invertir una matriz seleccionada
        arreglo = int(input("Ingresa grupo a invertir (1 o 2): ")) #pedimos cuál matriz
        if arreglo == 1: #si es igual a 1 invertimos filas por columnas en la matriz 1
            self.invertido = self.array1.transpose() #el resultado lo guardamos en otra variable
        elif arreglo == 2: #si es igual a 1 invertimos filas por columnas en la matriz 1
            self.invertido = self.array2.transpose() #el resultado lo guardamos en otra variable
        else: #si no es ni 1 ni 2 enviamos mensaje y retornamos el método
            print("Datos incorrectos, favor de verificar: ")
            return self.invertir()
        print("Grupo seleccionado invertido: \n",self.invertido) #mostramos el resultado
    
    def diagonal(self): #metodo para generar una diagonal de una matriz seleccionada
        arreglo = int(input("Ingresa grupo para diagonal (1 o 2): ")) #pedimos cuál matriz
        if arreglo == 1: #si es igual a 1 generamos la diagonal en matriz 1
            self.diagonal = np.diag(self.array1) #el resultado lo guardamos en otra variable
        elif arreglo == 2: #si es igual a 1 generamos la diagonal en matriz 2
            self.diagonal = np.diag(self.array2) #el resultado lo guardamos en otra variable
        else: #si no es ni 1 ni 2 enviamos mensaje y retornamos el método
            print("Datos incorrectos, favor de verificar: ")
            return self.invertir()
        print("Diagonal de grupo seleccionado: \n",self.diagonal) #mostramos el resultado
    
    def modificar(self): #metodo para modificar un elemento de una matriz seleccionada
        tamaño1 = self.array1.shape #obtenemos las dimensiones
        tamaño2 = self.array2.shape
        arreglo = int(input("Ingresa grupo a modificar (1 o 2): ")) #pedimos cuál matriz

        if arreglo == 1: #si es igual a 1 modifica matriz 1
            fila = int(input("Ingresa posición de fila (hay "+str(tamaño1[0])+"): ")) #pedimos cuál posición en filas 
            columna = int(input("Ingresa posición de columna (hay "+str(tamaño1[1])+"): ")) #pedimos cuál posición en columnas
            valor = int(input("Ingresa valor para esa posición: ")) #pedimos el valor nuevo para modificarlo
            self.array1[fila][columna] = valor #ingresamos posiciones y valor en matriz 1 para modificarlo
            print("Grupo modificado: \n",self.array1) #mostramos resultados

        elif arreglo == 2: #si es igual a 2 modifica matriz 2
            fila = int(input("Ingresa posición de fila (hay "+str(tamaño2[0])+"): ")) #pedimos cuál posición en filas 
            columna = int(input("Ingresa posición de columna (hay "+str(tamaño2[1])+"): ")) #pedimos cuál posición en columnas
            valor = int(input("Ingresa valor para esa posición: ")) #pedimos el valor nuevo para modificarlo
            self.array2[fila][columna] = valor #ingresamos posiciones y valor en matriz 2 para modificarlo
            print("Grupo modificado: \n",self.array2) #mostramos resultados
            
        else: #si no es ni 1 ni 2 enviamos mensaje y retornamos el método
            print("Datos incorrectos, favor de verificar: ")
            return self.invertir()

        repetir = input("¿Desea modificar otro elemento? (SI/NO): ").lower() #preguntamos si desea modificar otro elemento
        if repetir == "si": #si es si vuelva a ejecutar todo el método
            return self.agregar()

    def ganador(self):
        seleccion = random.randint(1, 2) #generamos un número random entre 1 y 2
        print("\nElección del ganador: ")

        if seleccion == 1: #si el número random es 1 toma la diagonal
            tamaño = len(self.diagonal) #leemos la longitud del vector
            ganador = random.randint(0, tamaño - 1) #pedimos un número ganador entre 0 y la longitud -1 para poder tomar alguna posición
            print ("¡El ganador es el número "+str(self.diagonal[ganador])+"!") #imprimimos el ganador con la diagonal indicando la posición aleatoria
        else: #caso contrario si toma dos
            tamaño = self.invertido.shape #obtenemos las dimensiones de la matriz invertida
            fila = random.randint(0, tamaño[0] - 1) #pedimos una fila entre 0 y el tamaño de la fila -1 para poder tomar alguna posición
            columna = random.randint(0, tamaño[1] - 1) #pedimos una columna entre 0 y el tamaño de la columna -1 para poder tomar alguna posición
            print ("¡El ganador es el número "+str(self.invertido[fila][columna])+"!") #imprimimos el ganador con la mtriz invertida indicando la fila y columna aleatoria

objeto= Arreglos()  #creamos el objeto que llame a la clase
objeto.crear_arreglos() #llamamos a cada método para que se ejecute 
objeto.eliminar()
objeto.agregar()
objeto.sumar_multiplicar()
objeto.modificar()
objeto.invertir()
objeto.diagonal()
objeto.ganador()