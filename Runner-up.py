if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    k=max(arr)
    newarr=[]
    for i in arr:
        if(i != k):
            newarr.append(i)         
    x=max(newarr)
    print(x)



# n=int(input())
#     ls1=list(map(int,input().split()))
#     ls2=list(set(ls1))
#     ls2.sort()
#     print(ls2[-2])