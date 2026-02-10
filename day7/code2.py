#Task 2: The Reshaper (Array Manipulation)
import numpy as np
arr=np.arange(24)
arr_3d=arr.reshape(4,3,2)
arr_transposed=arr_3d.transpose(0,2,1)
print("Final shape:", arr_transposed.shape)
print("Final array:")
print(arr_transposed)