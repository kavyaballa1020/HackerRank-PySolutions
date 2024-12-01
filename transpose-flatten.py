# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

N,M=map(int,input().split())
arr=[]

for i in range(N):
    arr.append(list(map(int,input().split())))
arr=np.array(arr)
result1=np.transpose(arr)
result2=arr.flatten()
print(result1)
print(result2)