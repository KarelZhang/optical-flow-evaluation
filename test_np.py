import numpy as np

a = [[-1,2,0,4,0,6],
     [6,0,4,-3,2,1]]

b = [[2,4,6,1,3,6],
     [1,2,3,4,5,6]]

a = np.reshape(a, (3,4))
b = np.reshape(b, (3,4))
print(a)
print(b)
mask = (a == 0)

b[mask] = 0

print(b)

