import numpy as np

# nditer => iterating
arr2=np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr2):
    print(x)
for x in np.nditer(arr2[:,::2]):
    print(x)

# ndenumerate
for idx, x in np.ndenumerate(arr2):
    print(idx,x)
arr1=np.array([1,2,3])
for idx, x in np.ndenumerate(arr1):
    print(idx,x)