import numpy as np
def matrices(col, row):
    lis2 = []
    for i in range(row):
        lis=[]
        for j in range(col):
            num = int(input("Valor [{}][{}]: ".format(i,j)))
            lis.append(num)
        lis2.append(lis)
    arr = np.array(lis2)
    print(arr)  
    return arr
def eleminar_col (mat):
    col = int(input("¿Que columna?(0/...): "))
    mat = np.delete(mat, col, axis=1)
    print(mat)
    print(mat.size)
    return mat
def multi(arr1, arr2, col, row):
    arr = np.zeros((col, row))

    for r in range(0, col):
        for c in range(0,row):
            for k in range(0,col):
                arr[r,c] += arr1[r,k] * arr2[k,c]
    
    return arr
def diagonal(arr):
    sus=0
    for i in range (len(arr)):
        sus +=  arr[i][i] 
    return sus
#Generador del primer arreglo
print("Arreglo 1")
col = int(input("Columnas: "))
row = int(input("Filas: "))
arr1 = matrices(col,row)
print("*******************************")
#Generador del segundo arreglo
print("Arreglo 2")
col2 = int(input("Columnas: "))
row2 = int(input("Filas: "))
arr2 = matrices(col,row)
arrs = np.zeros((col,row))
arrmu = np.zeros((col,row))
arri =  np.zeros((col,row))
arrdi = np.zeros((col,row))   
print("*******************************")
elim = input("¿Desea eliminar una columna?(s/n): ")
if (elim == "s"):
    cual= int(input("¿Cual arreglo?(1/2): "))
    if (cual == 1):
        arrm=eleminar_col(arr1)
    elif (cual == 2):
        arrm=eleminar_col(arr2)
    else:
        print("No hay ese numero de arreglo") 
else:
    arrm = arr2
print("*******************************")
print("Suma de matrices:")
arrs = arr1+ arrm
print (arrs)
print("*******************************")
print("Multiplicacion de matrices:")
arrmu = multi(arr1, arrm, col, row)
print(arrmu)
print("*******************************")
cual= int(input("¿Cual arreglo quiere invertir?(1/2): "))
if (cual == 1):
    arri = arr1[::-1]
elif (cual == 2):
    arri = arr2[::-1]
else:
   print("No hay ese numero de arreglo") 
print("arreglo invertido: ")
print(arri)
print("*******************************")
cual= int(input("¿Cual arreglo quiere sacar diagonal?(1/2): "))
if (cual == 1):
    arrdi = np.array(diagonal(arr1))
elif (cual == 2):
    arrdi = np.array(diagonal(arr2))
else:
    print("No hay ese numero de arreglo")
print("Diagonal del arreglo:")
print(arrdi)
uwu = input("Desea modificar algun valor?(s/n): ") 
while (uwu == "s"):
    col = int(input("¿Que columna?: "))
    row = int(input("¿Que fila?: "))
    valor = int(input("¿Que valor?: "))
    cual = int(input("¿De que arreglo?(1/2): "))
    if (cual == 1):
        arr1 [row][col] =  valor
    elif (cual == 2):
        arr2 [row][col] =  valor
    else:
        print("No hay ese numero de arreglo")