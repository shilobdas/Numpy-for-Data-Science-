import numpy as np
zeros_array = np.zeros((3, 4))
ones_array = np.ones((2, 5))
print("Array of Ones:\n", ones_array)

print("Array of Zeros:\n", zeros_array)
shape = zeros_array.shape
print("Shape of the array:", shape)
ndim = zeros_array.ndim
print("Number of dimensions:", ndim)