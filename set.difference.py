# Enter your code here. Read input from STDIN. Print output to STDOUT\
m=input()
ms=set(map(int,input().split()))
n=input()
ns=set(map(int,input().split()))
print(len(ms.difference(ns)))