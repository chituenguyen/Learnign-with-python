# Universal function
import numpy as np
x=[1,2,3,4]
y=[1,2,4,5]
z=np.add(x,y)
print(z)

# create Universal function == normal function
# 3 paramater (function, number of input, number of output)
def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))