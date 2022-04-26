def s(a,b):
   if a==b or abs(a-b)==5 or a+b==5:
       return True
   else:
       return False
a=int(input())
b=int(input())
print(s(a,b))