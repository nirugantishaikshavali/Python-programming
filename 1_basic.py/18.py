def sum1(a,b,c):
    if (a==b==c):
        n=(a+b+c)*a
    else:
        n=a+b+c        
    return n 
a=int(input())
b=int(input())
c=int(input())
print(sum1(a,b,c))