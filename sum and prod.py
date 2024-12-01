# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
arr=np.array(arr)
sum1=np.sum((arr),axis=0)
production=np.prod(sum1)
print(production)
