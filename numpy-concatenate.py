# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N,M,P=map(int,input().split())

array1=[]
array2=[]

for i in range(N):
    array1.append(list(map(int,input().split())))
array1=np.array(array1)
for i in range(M):
    array2.append(list(map(int,input().split())))
array2=np.array(array2)
result=np.concatenate((array1,array2),axis=0)
print(result)