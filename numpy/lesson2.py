import numpy as np

# Access 2-D array
arr2=np.array([[1,2,3,4],[4,5,6,7]])
print(arr2[0,1])
# Slice 2-D array
print(arr2[0,1:4])
print(arr2[0:2,1:3])
# d-type return type of data => covert type of data of array
print(arr2.dtype)
# Shape return a tuple with each index having the number of elements
print(arr2.shape)
new_arr=np.array([[1,23],[1,2],[1,2]])
print(new_arr.shape)
arr3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3.shape)