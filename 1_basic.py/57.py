import time
def sum1(n):
    strt=time.time()
    s=0
    for i in range(1,n+1):
        s+=i
    en=time.time()
    return s,en-strt
n=1000000000000000000000
print(sum1(n))