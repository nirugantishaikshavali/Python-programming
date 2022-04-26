#Abstraction-
# Hiding the implementation details from the user it shows the essential details.


# Module abc[By using abc module & import ABC,abstractmethod we implement the abstract class]
# ABC->abstract method->decorator
# # Abstract class ->which have Abstract methods
# Abstract method-> Method with declaration but not the definition.


# concrete class->class without abstact methods.
# object can't be instantiated for abstract class
# object can be instantiated for concrete class

#How we convert Abstract class to Concrete class?
# Concrete class(inherited from abstract class)
# ->Implement/Define all the absract methods,available in abstact class.

# there is only declartion part no defination part

from abc import ABC,abstractmethod
class whatsapp_owner(ABC):
       #decorector
    @abstractmethod
    def message(self):
        None
    @abstractmethod
    def emojic(self):
        None
#concreate class
class whatsapp_user(whatsapp_owner):
    def message(self):
        print("HELLO")
    def emojic(self):
            print("smile")
obj1=whatsapp_user()
obj1.message()
obj1.emojic()