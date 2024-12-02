# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
p=list(map(float,input().split()))
x=float(input())
print(np.polyval(p,x))