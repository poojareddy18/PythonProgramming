# importing Numpy
import numpy as np
# creating a random array of size 15, ranging from 1 to 20
x = np.random.randint(1,20,15,int)
# reshaping above array with 3*5 dimension
x = x.reshape((3,5))
print("An array of 3*5 dimension is :")
# printing out array x
print(x)
# considering the max value in a row and taking only one column in the axis
m = (x.max(axis=1).reshape(-1,1))
print("After reshaping :")
print(m)     # printing out array m
# creating an array where x==m (max value) and the remaining values will be 0
z = (np.where(x==m,x,0))
print("Max values in a row is :")
print(z)     # printing out array z
ans = (x-z)
print("replacing the max in each row by 0 :")  # printing remaining elements making max values 0
print(ans)
