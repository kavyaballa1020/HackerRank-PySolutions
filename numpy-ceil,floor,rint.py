# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy='1.13')

array1=np.array(list(map(float,input().split())))
print(np.floor(array1))
print(np.ceil(array1))
print(np.rint(array1))
