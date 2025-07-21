# NumPy Basics

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a + b =", a + b)
print("a * 2 =", a * 2)
print("sqrt(a) =", np.sqrt(a))

mat = np.array([[1, 2], [3, 4]])
print("Matrix:\n", mat)
print("Transpose:\n", mat.T)

# Broadcasting
c = np.array([10, 20])
print("Broadcasting mat + c:\n", mat + c)
