# Permulations
import numpy as np
from numpy import random

arr=np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

arr1=np.array([1,2,3,4])
arr2=random.permutation(arr1)
print(arr1,arr2)