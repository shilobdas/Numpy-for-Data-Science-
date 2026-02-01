import numpy as np
filled_array = np.full((4, 3), 12)
print("Filled Array:\n", filled_array)  
n_dim = filled_array.ndim
shape = filled_array.shape
print("Number of dimensions:", n_dim)
print("Shape of the array:", shape)