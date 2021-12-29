import numpy as np
from numpy import random
# random
x=random.randint(100,size=5)
print(x)
x1=random.randint(100, size=(2,5))
print(x1)
# random float return between 0 and 1
x3=random.rand(5)
print(x3)
x4=random.rand(2,4)
print(x4)
arr=[1,2,3,4]
x5=random.choice(arr,size=(2,4))
print(x5)

# Distribution
new_x= random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(10)) # probability doc lap voi nhau
print(new_x)