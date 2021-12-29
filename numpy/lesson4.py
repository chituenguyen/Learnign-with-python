import numpy as np

# Join in array
arr=np.array([1,2,3])
arr1=np.array([4,5,6])
# Concatenate
new_arr=np.concatenate((arr,arr1))
print(new_arr)
# Join 2-D array
a1 = np.array([[1, 2], [3, 4]])

a2 = np.array([[5, 6], [7, 8]])

a = np.concatenate((a1, a2), axis=1)
a = np.concatenate((a1, a2), axis=0)

print(arr)
# Join array using stack, hstack,vstack,dstack

# array_split

# search => where() method => side left or right

# Sort() method