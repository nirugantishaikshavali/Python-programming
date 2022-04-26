# def l(a,b):
#     if a>b:
#         z=a
#     else:
#         z=b
#     while(True):
#         if ((z%x==0) and (z%y==0)):
#             lcm=z
#             break
#         z+=1
#     return lcm
# x=15
# y=17
# print(l(x,y))

#gcd
def gcd(a,b):
    gcd=1
    if a%b==0:
        return b
    for i in range(int(b/2),0,-1):
        if a%i==0 and b%i==0:
            gcd=i
            break
    return gcd    
print(gcd(336,360))