def difference(a,b):
    if a>b:
        n=a-b
        r=n*2
    else:
        n=a-b
        r=abs(-n)
    return r    
a=int(input())
b=int(input())
print(difference(a,b))