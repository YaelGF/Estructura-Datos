#Ejemplos de declaracion
a= [1,2,3,4]
b= [6,7,8,9]

#c= [a,b]
c= [[1,2,3,4],
    [6,7,8,9]]

#Agregar datos
c.append([10,11,12,13])

#Visualizar contenido Matriz
for i in range(len(c)):
    for j in range(len(a)):
        print(c[i][j])