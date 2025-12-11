import scipy as sp
import numpy as np
from scipy import linalg

array1=np.array([[1,2],[3,4]])
array2=np.array([[5,9],[6,8]])

print(sp.linalg.solve(array1,array2))

function1=sp.linalg.inv(array1)
print(function1)