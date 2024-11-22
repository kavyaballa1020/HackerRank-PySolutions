if __name__ == '__main__':
    s = input()
    b1=b2=b3=b4=b5=False
    for i in s:
        if i.isalnum():
            b1=True
        if i.isalpha():
            b2=True
        if i.isdigit():
            b3=True
        if i.islower():
            b4=True
        if i.isupper():
            b5=True
    print(b1,b2,b3,b4,b5,sep="\n")
    
    