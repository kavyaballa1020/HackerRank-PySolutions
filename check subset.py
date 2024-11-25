# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    n=int(input())
    ns=set(map(int,input().split()))
    m=int(input())
    ms=set(map(int,input().split()))
    print(ns.issubset(ms))
