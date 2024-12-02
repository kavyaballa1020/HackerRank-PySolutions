# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N=int(input())
arr1=[]
arr2=[]
arr3=[]
for i in range(N):
    arr1.append(list(map(int,input().split())))
for i in range(N):
    arr2.append(list(map(int,input().split())))
arr1=np.array(arr1)
arr2=np.array(arr1)
arr3=np.dot(arr1,arr2)
print(arr3)