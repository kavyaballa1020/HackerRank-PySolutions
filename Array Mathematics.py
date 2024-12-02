# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N,M=map(int,input().split())
arr1=[]
arr2=[]
for i in range(N):
    arr1.append(list(map(int,input().split())))
arr1=np.array(arr1)
for i in range(N):
    arr2.append(list(map(int,input().split())))
arr2=np.array(arr2)
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1//arr2)
print(arr1%arr2)
print(arr1**arr2)
