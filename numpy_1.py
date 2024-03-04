import numpy as np 
#  using linespace(start,stop,number quantyty)
linesp = np.linspace(1,10,3)
# logspace same as linespace but with log numbers
logsp = np .logspace(1,20,3)

# arange(start,end,interval) its same as the above but only intervals and quantity that veries
array_range = np.arange(10,26,4)
print(array_range)

# creating array 
# you must use array in order to make list of numbers used as array
number_list = np.array([1,2,3,4,5,6,7,9,8,])

#  you can make a matricx with it as well
mat = np.reshape(number_list,(3,3))
print(mat)

# to make such array you need barckets inside the array bracket[ [],[],[]]
mat2 = np.array([[1,2,3],[4,5,6],[7,6,9]])
print(mat2)

# perform mathematical operations 
print(mat ** 3)

# Transpose and inverse matrics
print(mat2.transpose()) # make it transpose matrics

mat2_inv =np.linalg.inv(mat2)
print(mat2.dot(mat2_inv)) 

# Indexing and updationg the array 
#  the order is Row Colm array[0] or array[the position]

print(f"""
      The index start with zero as first position 
      and -1 as last position """)
print(mat)
print(mat[(2,2)])

mat[2,2] = 2 # Updating the selected value as in normal list
print(mat)

# to select range in the row or colum use [fist:last]

# example the whole vertical second col
mat[:,1] = 0
print(mat)

# replacing by anther matrix
new = np.zeros((3,3),dtype=float)
mat3 = np.ones((5,5),dtype = int)
mat3[1:-1,1:-1] = new  # updation indexed array with a new array of the same R&C
print(mat3)


