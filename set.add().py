# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
k=set()
for i in range(0,n):
    s=input()
    k.add(s)
print(len(k))
