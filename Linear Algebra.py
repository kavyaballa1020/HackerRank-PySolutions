import numpy as np
N=int(input())
A=[]
for i in range(N):
    A.append(list(map(float,input().split())))
A=np.array(A)
print(round(np.linalg.det(A),2))