# Inheritance:-One class acquiring the properties of another class.
# *In Inheritance we have parent class[Base] and child class[Dervied].

# Here we 5 Inheritances
# 1.single-Inheritance:-This dervied class acquring the properities of base class.
# 2.Multilevel-Inheritance:-one base class and dervied class [parent class]-> subclass[child class]. 
# 3.Hierarihical-Inheritance-one base class and two dervied classes.
# 4.Multiple-Inheritance:- two base classes and one dervied class.
# 5.Hybird-Inheritance:-One base class and two derived class and one base class. 

#1.single inheritance:
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Student(Person):
    def __init__(self,rollno,name,age,per):
        self.rollno=rollno
        self.name=name
        # Person.__init__(self,name,age)
        self.age=age
        self.per=per
    def display(self):
        print("Rollno:",self.rollno)
        Person.display(self)
        print("Per:",self.per)

obj1=Student(1,"shaik",22,82)
print("Student details:")
obj1.display()

o/p:-
Student details:
Rollno: 1
Name: shaik
Age: 22
Per: 82
'''

# 2.multiple-inheritance
'''
class subject:
    def __init__(self,sub_name):
        self.sub_name=sub_name
class teacher(subject):
    def __init__(self, sub_name,teacher_name):
        super().__init__(sub_name)
        self.teacher_name=teacher_name
class student(teacher):
    def __init__(self,roll_no,name,teacher_name,sub_name):
        self.roll_no=roll_no
        self.name=name
        super().__init__(sub_name, teacher_name)
        
    def get_values(self):
        return (self.roll_no,self.name,self.teacher_name,self.sub_name)

obj1=student(1,"A","AAA","Maths")
obj2=student(1,"B","BBB","Physics")
obj3=student(1,"C","CCC","Chemistry")

r=obj1.get_values()
print("student 1 result:",r)

r=obj2.get_values()
print("student 1 result:",r)

r=obj3.get_values()
print("student 1 result:",r)

# o/p:-
# student 1 result: (1, 'A', 'AAA', 'Maths')
# student 1 result: (1, 'B', 'BBB', 'Physics')
# student 1 result: (1, 'C', 'CCC', 'Chemistry')
'''
 

# 3.Hierarihical Inheritance:-
'''
class subject:
    def __init__(self,sub_name):
        self.sub_name=sub_name
class maths(subject):
    def __init__(self, sub_name,name,marks):
        self.name=name
        self.marks=marks
        super().__init__(sub_name)
    
class social(subject):
    def __init__(self, sub_name,name,marks):
        super().__init__(sub_name)
        self.name=name
        self.marks=marks
s1=social("social","shaik",78)
s2=social("social","rahul",95)

m1=maths("maths","A1",98)
m2=maths("maths","B3",76)

print("student1 records:")
print(s1.sub_name,s1.name,s1.marks)
print(m1.sub_name,m1.name,m1.marks)

print("\n")
print("student2 records:")
print(s2.sub_name,s2.name,s2.marks)
print(m2.sub_name,m2.name,m2.marks)
'''
'''
o/p:
student1 records:
social shaik 78
maths A1 98


student2 records:
social rahul 95
maths B3 76
'''


#4.Multiple Inheritance
'''
class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add1(self):
        return self.a+self.b
class Subtraction:
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def sub1(self):
        return self.c-self.d
class multiplication(Addition,Subtraction):
    def __init__(self,a,b,c,d):
        Addition.__init__(self,a,b)
        Subtraction.__init__(self,c,d)
    def mul(self):
        return self.a*self.c
    
m=multiplication(30,40,10,20)
a=m.add1()
s=m.sub1()
mu=m.mul()
print("Addition of two numbers:",a)
print("Subtraction of two numbers:",s)
print("Multiplication of two numbers:",mu)
'''


'''
#5.hybrid class

class A:
    def __init__(self,w):
        self.w=w
        print("At init of class A")

class B:
    def __init__(self,w,x,y):
        self.x=x
        print("At init of class B")
        super(B,self).__init__(w,y)


class C(A):
    def __init__(self, w,y):
        self.y=y
        # B.__init__(self,b) 
        super(C,self).__init__(w)
        print("At init of class C")

class D(B,C):
    def __init__(self, w,x,y,z):
        self.z=z
        super(D,self).__init__(w,x,y)
        print("At init of class D")

d=D(1,2,3,4)
print(D.mro())

o/p:-
At init of class B
At init of class A
At init of class C
At init of class D
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
'''
