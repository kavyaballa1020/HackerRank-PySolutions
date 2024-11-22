# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
ns=set(map(int,input().split()))
m=int(input())
ms=set(map(int,input().split()))
print(len(ns.union(ms)))
