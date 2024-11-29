# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
ns=set(map(int,input().split()))
k=int(input())
for i in range(k):
    ls=input().split()
    if ls[0]=="pop":
        ns.remove(min(ns))
    elif ls[0]=="remove":
        try:
            ns.remove(int(ls[1]))
        except KeyError:
            pass
    elif ls[0]=="discard":
        ns.discard(int(ls[1]))
print(sum(ns))