import numpy as np
arr = np.array([1,2,3])
print(type(arr))
print(arr)
arr1=np.array((1,2,3))
print(arr1)
# 2-D array
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
# 3-D array
arr3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3)
# check number dimensions
print(arr1.ndim)
print(arr2.ndim)

# Covert number of dimensions
a=np.array([1,2,3],ndmin=2)
print(a)