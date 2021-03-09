import numpy as np
#diagonal

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
sus = 0

for i in range (len(arr)):
    sus +=  arr[i][i] 
print(sus)