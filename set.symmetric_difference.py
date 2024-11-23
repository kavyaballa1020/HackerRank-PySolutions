# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
ns=set(map(int,input().split()))
m=input()
ms=set(map(int,input().split()))
print(len(ms.symmetric_difference(ns)))