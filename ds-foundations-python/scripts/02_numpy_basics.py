# NumPy Basics
# NumPy (short for Numerical Python) is a Python library that makes working with numbers, 
# especially arrays and matrices, fast and easy.
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a + b =", a + b)
print("a * 2 =", b * 2)
print("sqrt(a) =", np.sqrt(a))

mat = np.array([[1, 2], [3, 4]])
print("Matrix:\n", mat)
# In transpose (rows become columns):
print("Transpose:\n", mat.T)

# Broadcasting
c = np.array([10, 20])
print("Broadcasting mat + c:\n", mat + c)


"""
Efficient storage and processing of large numerical data.
Supports multi-dimensional arrays (like lists, but faster and more powerful).
Provides mathematical functions for operations on arrays — e.g., addition, multiplication, 
statistics, linear algebra.
Much faster than using Python’s built-in lists for numerical calculations because it’s 
implemented in C under the hood.
"""