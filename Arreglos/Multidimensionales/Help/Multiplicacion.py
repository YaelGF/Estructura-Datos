import numpy as np
#multiplicacion
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.array([[9,8,7],[6,5,4],[3,2,1]])

arr = np.zeros((3,3))

for r in range(0,3):
    for c in range(0,3):
        for k in range(0,3):
            arr[r,c] += arr1[r,k] * arr2[k,c]
print(arr)