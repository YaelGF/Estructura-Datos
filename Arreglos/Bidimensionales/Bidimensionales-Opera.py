import numpy
 #Operaciones

#arreglo a lista
a = numpy.array([1, 2, 3, 4, 5])
print("Array to list = ", a.tolist())

#eliminacion de fila o columnas
a = numpy.array([[1, 2, 3], [4, 5, 6], [10, 20, 30]])
newArray = numpy.delete(a, 1, axis = 0)#axis 0 = fila 1 = columnas
print(newArray)

#Eliminacion de elemento
a = numpy.array([1, 2, 3])
newArray = numpy.delete(a, 1,)
print(newArray)

#Insertar
a = numpy.array([1, 2, 3])
newArray = numpy.insert(a, 1,90)
print(newArray)

#fusion de listas
a = numpy.array([1, 2, 3, 4, 5])
b = numpy.array([10, 20, 30, 40, 50]) 
newArray = numpy.append(a, b)
print("The new array = ", newArray)