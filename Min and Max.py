# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
arr=np.array(arr)
mini=np.min(arr,axis=1)
print(np.max(mini))