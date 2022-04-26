# class:-It is a set of statements which contains variables and methods is called class
# It is blueprint which is followed by hte objects.

# object:-It is a instance of class



'''
class employee:
    id=123#instance variable
    place="bangolre"
    
    def work(self):
        place="mysore" #local variable
        print("current base location:",place)
        print("previous base location:",self.place)
obj=employee()
print("id=",obj.id)
print("place=",obj.place)
obj.work()
'''

class employee:
    #constructor
    def __init__(self,id,place):
        self.id=id
        self.place=place
    
    def work(self):
        place="mysore"
        print("current base location:",place)
        print("previous base location:",self.place)
   
obj=employee(int(input("Enter the id:")),input("Enter the place:"))
print("id=",obj.id)
print("place=",obj.place)
obj.work()

# o/p:-
# Enter the id:123
# Enter the place:bangolre
# id= 123        
# place= bangolre
# current base location: mysore
# previous base location: bangolre