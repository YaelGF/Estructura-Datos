import numpy as np
#Eliminar Columnas
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat = np.delete(mat, 2, axis=1)
print(mat)