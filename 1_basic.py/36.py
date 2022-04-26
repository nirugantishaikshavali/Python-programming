def a(x,y):
    if not (isinstance(x,int)) and isinstance(y,int):
        return "input must be integers"
    return x+y
    
x=3
y=9
print(a(x,y))