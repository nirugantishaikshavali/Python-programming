#polymorphism:-Implementing the same thing in different ways.
# ->Methods with same name but implementing in different ways.
# ->polymorphism deals with methods.
# ->It can be achieved in two ways.1.Method Overloading
                                #  2.Method Overriding.
                                 
                                 
# 1.Method Overloading:-
# ->Method name should be same but arguments must be different.


'''
class MethodOverloading:
    def display(self,a=None,b=None):
        print(a,b)
obj1=MethodOverloading()
obj1.display()
obj1.display(4)
obj1.display(5,9)
'''

# 2.Method Overriding:-
# ->Method name should be same and argument must be same.

class father:
    def phone(self):
        print("Noikia")
class son(father):
    def phone(self):
        print("iphone")
obj1=son()
obj1.phone()
        