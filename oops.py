# OOPS IN PYTHON

# 1. Basic of OOP
# 2. Types of variables and methods. 
# 3. Inheritance 
# 4. Polymorphism
# 5. Encapsulation
# 6. Abstraction
# 7. Interface
# 8. Mini Project OOPS
# 9. Interview Preparation

# Programming Paradigms  

# Ways of organizing programs.  
# Python supports multiple paradigms. These are as follows:-  
  
# 1) Procedural oriented paradigm    -- Line by Line Execution of Code, reusability not there
  
# 2) Functional oriented paradigm  -- Calling and reusability
  
# 3) Object-oriented paradigm  -- real life examples we solved

# object

# An object in OOP represents real-life objects.
# ex. Email, man, student, employee etc.

# Every object has two properties.

# 1) attributes
# 2) Behaviours

# Attributes:- heading, subject, name, recipients list -- data
# Behaviours:- sending, Adding attachments [action]

# employee attributes are email id, Name
# behaviours means employee getting bonus

# What is Object-Oriented Programming (OOP) ?

# Object-oriented programming is an approach of writing programs by creating classes and objects.
# More focus is on data rather than logic.

# Why OOP

# To solve real-world problems effectively.

# OOP provides some features :-

# 1) Inheritance :- reusability
# 2) encapsulation :- data security
# 3) abstraction :- Data hiding
# 4) polymorphism

# Bank Account - Object Money - attribute(data) and money add hona, deduct hona (Action)

# What is class?

# Class is a template/blueprint/model/prototype for creating objects

# Object is real life entity

# Every object belong to same class
    
# Email class
#     email1 + email2 + email3    -- object

# What is class?

# Class is a collection of attribute and methods.

# class is a collection of objects.

# Technically class is a user defined data type.

# attributes:-
# heading
# participants
# attachments

# methods:-

# send()
# save_as_draft()

# Email1:-

# heading:- taking leave
# participant:- xyz
# attachments:- form.pdf

# Email2:-
# heading:- require help
# participant:- abc
# attachments:- pic.jpg

# All 14 data types are built in data types

# x = 100

# print(type(x)) -- class -- int

# def demo():
#     print("hello")

# print(type(demo))  -- class -- function -- bulit in function

# employee, student this we will create own its called user defined function.

# Creating Class and Objects ?

# class Class_name:
#     #attributes (Variables)
#     #methods (functions)

# obj1 = Class_name([args])
# obj2 = Class_name([args])

# class Email:  # Class -- User defined data type
#     pass

# e1 = Email() # Object1
# e2 = Email() # Object2

# print(type(e1))
# print(type(e2))

# # Constructor and types of Constructor

# class Employee:
#     def __init__(self):  # Special method or magic method
#         self.salary=2000
#         self.age=21

# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)

# What is constructor?

# Special method used for initializing objects with attributes
# It is __init__ method
# First arguments is self.

# Types of constructor?

# Parameterized constructor
# Non-Parameterized constructor
# Default Constructor

# class Employee:
#     pass

# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)

# Non-Parameterized Constructor

# class Employee:
#     def __init__(self):  # Non-Parameterized Constructor
#         self.salary=2200
#         self.age=28

# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)

#  Non-Parameterized Constructor

# class Employee:
#     def __init__(self,sal,ag):  # Special method or magic method
#         self.salary=sal         # Parameterized constructor
#         self.age=ag 

# e1 = Employee(24000,21)
# e2 = Employee(26000,26)
# print(e1.__dict__)


# class Employee:
#    pass

# e1 = Employee()   # Default Constructor
# e2 = Employee()
# print(e1.__dict__)

# # without constructor: object cannot be created

# ----------------------------------------------------

# What is self?
# self is a variable in that memory address of current object

# 1. Memory allocation for object - heap memory allocate honga
# 2. memory reference returned to the object
# 3. memory reference automatically passed inside constructor
# 4. constructor creates/initialize variables at that memory reference.

# class Employee:
#     def __init__(self,sal,ag):  # Special method or magic method
#         self.salary=sal         # Parameterized constructor
#         self.age=ag     # in the self present is memory location of e1 and e2 object

# e1 = Employee(24000,21)
# e2 = Employee(26000,26)


# Accessing Class Members Outside the Class
 
# Class members:- Attributes(variables) + Actions(Methods and functions) inside the class.

# We can access these variables using object outside the class.

# Syntax:-
#     Accessing attribute:- object_name.variable_name
#     Accessing method:- object_name.method_name()

# class Employee:
#     def __init__(self,sal,ag):
#         self.salary=sal   # attribute
#         self.age=ag

#     def display(self): # instance method/ # Special method or magic method
#         print(f"Salary is {self.salary} and age is {self.age}") #   Parameterized constructor

# e1 = Employee(24000,21)
# e2 = Employee(26000,24)

# # accessing attribute outside the class

# print(e1.salary) # 24000
# e1.salary = 34000 # updating attribute/salary
# print(e1.salary)

# e2.display()

# Following are the build -in class functions:-

# getattr(object_name, attribute_name)
# setattr(object_name, attribute_name, new_value)
# delattr(object_name, attribute_name)
# hasattr((object_name, attribute_name))

# class Employee:
#     def __init__(self,nm,ag):
#         self.name = nm
#         self.age = ag

# e1 = Employee('raj',21)
# e2 = Employee('jay',22)

# print(getattr(e1,'age')) # 21
# setattr(e2,'name','jayraj') # jayraj
# print(e2.__dict__)
# delattr(e2,'age')
# print(e2.__dict__)

# print(hasattr(e1,'name'))


# oops -- object oriented programming
# - four pillers/features

# - inheritance:- property
# - polymorphism:- One person many behaviour
# - abstraction:- ATM
# - encapsulation:- laptop/capsule

# class Classname:
    # methods
    # variables

# methods

# - instance method
# - staticmethod
# - classmethod
# # variables
# - instance variable
# - static variable/class level variable

# class Student:
#     pass

# s1 = Student() # Object create karna.
# print(type(s1))

# class Electronics:
#     pass

# s1 = Electronics() # Object create karna.
# print(type(s1))


# class Student: # class/model/category
#     def __init__(self): # instance method 
#         print("init method")
#         pass

# # referencce variable

# # dunder methods/magicmethods
# s1 = Student() # Object create karna/instantiate/instance create krna.
# print(s1.__dict__) # {} # special variable809

# class Student:
#     def __init__(self):
#         pass

# s1 = Student() # Student class ka object hai
# print(s1.__dict__) # {}
# s1.name = "Aayush"
# s1.age = 25

# print(s1.__dict__) 

# class Student:
#     def __init__(self, sid, sname, sage, smarks):
#         self.ID = sid
#         self.name = sname
#         self.age = sage
#         self.marks =  smarks

# s1 = Student(sid=101, sname="A", sage=25, smarks=69)
# s2 = Student(sid=102, sname="B", sage=23, smarks=98)
# s3 = Student(sid=103, sname="C", sage=24, smarks=36)

# print(s1)
# print(s2)
# print(s3)

# DRY -- 
# stud_lst = [s1.__dict__, s2.__dict__, s3.__dict__]
# # print(stud_lst)
# for i in stud_lst:
#     print(i)

# class Student:
#     def __init__(self, sid, sname, sage, smarks):
#         self.ID = sid
#         self.name = sname
#         self.age = sage
#         self.marks =  smarks

#     def __str__(self):
#         return "Hiiii"

# s1 = Student(sid=101, sname="A", sage=25, smarks=69)
# s2 = Student(sid=102, sname="B", sage=23, smarks=98)
# s3 = Student(sid=103, sname="C", sage=24, smarks=36)

# print(s1)
# print(s2)
# print(s3)

# class Student:
#     def __init__(self, sid, sname, sage, smarks):
#         self.ID = sid
#         self.name = sname
#         self.age = sage
#         self.marks =  smarks

#     def __str__(self):
#         return f"{self.__dict__}"

# s1 = Student(sid=101, sname="A", sage=25, smarks=69)
# s2 = Student(sid=102, sname="B", sage=23, smarks=98)
# s3 = Student(sid=103, sname="C", sage=24, smarks=36)

# print(type(s1))
# print(s2)
# print(s3)

# class Student:
#     def __init__(self, sid, sname, sage, smarks):
#         self.ID = sid
#         self.name = sname
#         self.age = sage
#         self.marks =  smarks

#     def __str__(self):
#         return f"{self.__dict__}"
    
#     def __repr(self):
#         return str(self)

# s1 = Student(sid=101, sname="A", sage=25, smarks=69)
# s2 = Student(sid=102, sname="B", sage=23, smarks=98)
# s3 = Student(sid=103, sname="C", sage=24, smarks=36)

# stud_lst = [s1, s2, s3]
# print(stud_lst)


# MRO (Method Resolution Order)

# MRO represents how properties (attributes + methods) are searched in inheritance.

# Rule -01

# Python first search in child class and then goes to parent class
# Priority to child class

# Rule -02

# MRO follows 'Depth first left' to 'Right approach'

# Rule - 03

# You can use MRO() method for knowing mro of any object.

# class A:
#     pass

# class B:
#     pass

# class C:
#     pass

# class X(A,B,C):
#     pass

# class Y(B,C):
#     pass

# class P(X,Y):
#     pass

# print(P.mro())


# # What is Encapsulation in Python?

# # Wrapping up data and methods working on data together in a single unit (i.e class) is called as Encapsulation

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print(f"name is: {self.name} and salary is: {self.salary}")


# super key
# super ek temporary instance hai wo parent method ko call krta hai use super key kahate hai
# multilevel inheritance
# class A: 
#     def m1(self):
#         print("in A-m1")

# class B(A):
#     def m1(self):
#         print("in B-m1")

# class C(B):
#     def m1(self):
#         print("in C-m1")

# class D(C):
#     def m1(self):
#         super().m1()
#         print("in D-m1")
        
# obj = D()
# obj.m1()


# class A: 
#     def m1(self):
#         print("in A-m1")

# class B(A):
#     def m1(self):
#         print("in B-m1")

# class C(B):
#     def m1(self):
#         print("in C-m1")

# class D(C):
#     def m1(self):
#         super().m1()
#         print("in D-m1")
        
# obj = D()
# obj.m1()

# class Parent:
#     def show(self):
#         print("Parent class method")

# class Child(Parent):
#     def show(self):
#         print("Child class method")
#         super().show() # Calling parent class method

# # Usage
# obj = Child()
# obj.show()


# class A:
#     def __init__(self, var1):
#         print("in A")
#         self.var_1 = var1

# class B(A):
#     def __init__(self):
#         print("in A")

# obj = B()


# class A:
#     def __init__(self, var1):
#         print("in A")
#         self.var_1 = var1

# class B(A):
#     pass

# obj = B(10)

# has and is relation


# KISS -- Keep It Simple Stupid

# Plymorphism in python is an ability of python object to take many forms.

# If a variable, object, method performs diff behaviour according to situation is called as polymorphism.

# +, -, % python object

# print(10+20) # 30

# print("hello"+"world") #helloworld

# len function

# according to the situation behave differently

# len("hello") # count the number of characters

# len(['h', 'e', 'l', 'llo']) #3 # count the no. of items.

# len(dictionary) # number of keys

# reversed

# emp = ["jay", 'viru', 'ram']
# company = 'infosys'

# for i in reversed(company):
#     print(i)

# print("for list now:")
# for i in reversed(emp):
#     print(i)


# Example

class veh:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def get_details(self):
        print("name is:",self.name)
        print("color is:",self.color)
        print("price is:",self.price)

    def max_speed(self):
        print("maximum speed limit is 100")

    def gear(self):
        print("gear change is 6")





