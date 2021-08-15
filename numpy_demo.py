# numpy - linear algebra library

# casting python lists to np arrays

my_list = [1,2,3]
import numpy as np

my_array = np.array(my_list) # cast normal list to np array

print(my_array)

print(type(my_array))

my_mat = [[1,2,3],[4,5,6],[7,8,9]]

my_3d_array = np.array(my_mat)

print(my_3d_array)

# using ranges & np inbuilt functions

print(np.arange(0,11,2)) # [ 0  2  4  6  8 10]

print(np.zeros((2,3)))
print(np.ones((3,3)))

