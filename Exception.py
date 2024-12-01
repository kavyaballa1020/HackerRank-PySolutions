# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    try:
        a,b=map(int,input().split())
        c=a//b
    except ZeroDivisionError as e1:
        print("Error Code:",e1)
    except ValueError as e2:
        print("Error Code:",e2)
    else:
        print(a//b)