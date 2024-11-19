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
