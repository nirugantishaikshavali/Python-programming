def gcd(a,b):
    gcd=1
    if a%b==0:
        return b
    for i in range(int(b/2),0,-1):
        if a%i==0 and b%i==0:
            gcd=i
            break
    return gcd
a=4
b=6
print(gcd(a,b))
