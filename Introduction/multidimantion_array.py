import numpy as np

# Creating a 3D array (2 matrices, each 2x3)
three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], 
                        [[7, 8, 9], [10, 11, 12]]])

print("Shape:", three_d_arr.shape)    # Outputs: (2, 2, 3)
print("Dimension:", three_d_arr.ndim) # Outputs: 3
