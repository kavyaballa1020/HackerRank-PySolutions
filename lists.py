if __name__ == '__main__':
    N = int(input())
    k=[]
    for i in range(N):
        ls=input().split()
        if ls[0]=="insert":
            k.insert(int(ls[1]),int(ls[2]))
        elif ls[0]=="print":
            print(k)
        elif ls[0]=="remove":
            k.remove(int(ls[1]))
        elif ls[0]=="append":
            k.append(int(ls[1]))
        elif ls[0]=="sort":
            k.sort()
        elif ls[0]=="pop":
            k.pop()
        elif ls[0]=="reverse":
            k.reverse()
        else:
            print(k)
        
        
        