# encapsulation:-wrapping of data and functions  into single entity is called encapsulation.
# ->By using Access specifiers-1.Private specifier->Accessed by only class .
#                              2.Public specifier->Accessed by any class and function or class inherited
#                              3.Protected specifier->Accessed by only class.

#scope
# a=1 ->public variable
# a=__1->private variable


#public variable,method
''''
class encp:
    a=1
    def value(self):
        print("hello")
obj1=encp()
print(obj1.a)
obj1.value()

#private variable
class encp:
    __a=1
    def value(self):
        print(self.__a)
        print("hello")
obj1=encp()
obj1.value()
'''

#private variable,method
class encp:
    __a=1
    
    def __value(self):
        print(self.__a)
        print("hello")
    def show(self):
        self.__value()
obj1=encp()
obj1.show()
