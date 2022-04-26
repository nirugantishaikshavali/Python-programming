def sum1(a,b):
    s=a+b
    if s in range(15,20):
        return 20
    return s
a=int(input())
b=int(input())
print(sum1(a,b))