# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(map(int,input().split()))
n=int(input())
b=True
for i in range(n):
    ns=set(map(int,input().split()))
    if not A>ns:
        b=False
        break
print(b)
