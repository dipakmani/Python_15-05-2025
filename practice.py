# Python is dynamically programming language
# Python is a purely oop langauge.

# # # print("Hello World")

#print("Hello World")

#Python code works line by line execution

# ctr + ?

# PEP8 Rules

"""
print("######")
a = 10
print(a)
b = 20
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a-b)
print(a/b)
print(a//b)
print("######")
"""

"""
a = 10 # integer
print(a)
a = 10.25 # float
print(a)
a = 10 + 2j # complex
print(a)

a = "ab56c@d" # string
print(a)
a = [10, 20, 10.25, "abcd", 3+8j, "azcd"] #list square bracket
print(a)
a = (10, 20, 10.25, "abcd", 3+8j, "azcd") # tuple parenthesis
print(a)
a = {10, 20, 30, 40} # set curly bracket
print(a)
a = {"name": "Dipak", "city": "Pune", "age": 27} # key value separated by colon it's disctionary
print(a)

"""

# know the rules of identifier

# var = 10
# var = 20
# var = "Python"
# var = [1, 2, 3, 4]

# n1 = 10
# n2 = 20

# no any special char except understore
# can not start with number
# can not start or used for a reserved keyword as a variable
# identifiers are case sensitive


# Meaningful name

# a_10 = 90000
# 10_ee = 50 error will occur

# import keyword

# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
#  'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',

# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# if = 20 # we can't use as a identifier and variable
# with = 200
# iff = 10  # we can use this

a = [1,2,3,"abc"]
print(dir(a))


# python is dynamically typed need not neccessary to put in or float for a variable defined

"""
a = "ab56c@d" # string
print(type(a))
a = [10, 20, 10.25, "abcd", 3+8j, "azcd"] #list square bracket
print(type(a))
a = (10, 20, 10.25, "abcd", 3+8j, "azcd") # tuple parenthesis
print(type(a))
a = {10, 20, 30, 40} # set curly bracket
print(type(a))
a = {"name": "Dipak", "city": "Pune", "age": 27} # key value separated by colon it's disctionary
print(type(a))

"""

# build in function

# type()
# print()
# len()

# Type of error
# Syntax error
# IndexError
# Type error


# Data Types in Python 

# datatype is just a category of data.
# It defines possible operations:- 10, "dipak"

# Below are datatypes available in python.
# - Numeric types:- int, float, complex (special type) 
# - Sequence types:- str, list, tuple
# - Mapping types:- dict
# - Set types: set, frozenset
# - Boolean types: bool
# - Binary types: bytes, bytearray

# - None type: None
# int  10, 20, 30, 40 -- immutable
# float 10.24, 100.00 -- immutable
# complex 10+2j, 5j -- immutable

# str  "", "sanket", "aasds", "a", "10" -- immutable
# list [" "] [1,2,3, "addss", [7,8,9]] -- mutable
# tuple () (1,2) -- immutable
# set {1,2,3} -- mutable
# frozenset -- frozenset({1,2,3}) -- immutable
# range 1,10 -- immutable

# dict {"key": "value"} -- mutable
# None None -- immutable
# bool: True, False -- immutable

# bytearray -- mutable

# bytes -- immutable

# operand
# operator

# Operators in Python

# print(3 + 2)   # addition(+)
# print(3 - 2)   # subtraction(-)
# print(3 * 2)   # multiplication(*)
# print(3 / 2)   # division(/)
# print(3 ** 2)  # exponential(**)
# print(3 % 2)   # modulus(%)
# print(3 // 2)  # Floor division operator(//)
# # Variables
# # Variables are containers for storing data values.


# list
# []
# homo+hetro
# list is mutable
# index based operation
# list allows all data type
# list allows duplicates values
# insertion order maintain 
# IndexError: list index out of range

# l2 = [10, 20, "aa", "aa", 10] # insertion order naintained
# print(l2)

# lst = [100, 200, 300, 400]

# lst[0] = "aa"

# del lst[0]

# print(lst)

# print(lst[1])
# print(lst[2])
# print(lst[-1])
# print(lst[-0])


# lst[0] = 10
# lst[-1] = 450

# print(lst)

# lst1 = [10, 10.25, 20+5j, [4, 5, 6], {7,8,9}, {"a": "apple", "b": "ball"}, None, True, False, range(1,10),
# frozenset({8, 5, 9}), bytearray([1, 2, 3]), bytes([6, 5, 9])]

# print(lst1)
   
# [1, 2, 3, 4, 5, "aaa"] - hetrogenous

# [1, 10.25, "aaa"] - hetrogenous

# [1, 2, 3, 4, 5] --homo
# index -- +ve and -ve

# print("-----------------------------------------------------------")

# tuple -- immutable version of list
# ()   or (10, )
# homo+hetro
# list is im-mutable
# index based operation
# tuple allows all data type
# list allows duplicates values
# insertion order maintain 
# TypeError: 'tuple' object does not support item assignment

# t1 = (10, 20, 30, 40)

# t1[0] = 1000 # TypeError: 'tuple' object does not support item assignment
# print(t1[0])
# print(t1, type(t1))

# print("-----------------------------------------------------------")


# set
# set() - empty lst
# homo+hetro
# set is mutable # change and add kar sakte hai
# doesn't maintain insertion order
# doesn't allow duplicates
# no index based operation
# allows only immutable data types
# set is not allow the list


# s1 = {10, "20", 20.5}
# print(s1)
# set is mutable

# s1.clear()
# print(s1)

# s2 = {10, 10.25, 20+5j, None, True, False, range(1,10),
# frozenset({8, 5, 9}), bytes([6, 5, 9]),}
# print(s2)

# print(s2[0])  # TypeError: 'set' object is not subscriptable not allowed


# Range

# r1 = range(1, 10)
# print(r1, type(r1))

# r1 = range(1, 11, 1) # (start, end, stepsize) - end is excluded
# print(list(r1))
# print(r1, type(r1))

# r1 = range(1, 11, 2) # (start, end, stepsize) - end is excluded
# print(list(r1))
# print(r1, type(r1))


# dict
# {} - empty dict
# no index based operation d1[0]  error will came
# key duplicates not allowed
# values duplicates allowed
# Insertion order maintain
# keys should only be immutable
# values can be mutable or immutable
# we can't take key as a [1, 2, 3]  -- list

# d1 = {"name": "sanket", "surname": "lokhande", "age": 27, "salary" : 85000, "address": "Mumbai"}
# # print(d1, type(d1), 10)

# print(len(d1))
# print(d1["name"])
# # print(d1["Address"])  # KeyError: 'Address'
# d1["perm address"] = "Pune"
# print(d1)
# d1["age"] = 28
# print(d1)
# d1["address"] = "Pune" 
# print(d1)


# d2 = {[1,2,3]: "apple"}
# print(d2)    # TypeError: unhashable type: 'list'

# d2 = {"a": "apple"}
# print(d2) 


# # Creating Variables
# # Python has no command for declaring a variable.

# # A variable is created the moment you first assign a value to it.


# # Variable Names
# # A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# # Rules for Python variables:

# # A variable name must start with a letter or the underscore character
# # A variable name cannot start with a number
# # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# # Variable names are case-sensitive (age, Age and AGE are three different variables)
# # A variable name cannot be any of the Python keywords.

# myvar = "Kartik"
# my_var = "Kartik"
# _my_var = "Kartik"
# myVar = "Kartik"
# MYVAR = "Kartik"
# myvar2 = "Kartik"


# # print(1+1)

# # s = "ram ram"
# # print(s[:3])



# # # know the rule of identifiers

# # var = 10
# # var = 20
# # var= "Python"
# # var = [1, 2, 3, 4]

# # n1 = 10
# # n2 = 30

# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # print(1964)

# type casting
# Converting the value of one type type to another type is called 'type casting' or 'type conversion'
# Implicit type conversion
# Explicit type conversion

# Implicit type conversion

# Implicit type conversion, python automatically converts one data type to another data type
# Generally, python promotes conversion of lower data type to higher data type to avoid data loss.

# x = 123 # int
# y = 1.23 # float
# z = x + y # float
# print(z)
# print(int(z))

# int, float, str

# x = 123
# y = "1.23"       # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# z = x + y        
# print(z)

# Explicit type conversion

# Programmer converts one data type to another data type.
# We have predefined functions for explicit type conversion. 

# This are the pre defined function converts into explicit function

# int(value)
# float(value)
# str(value)
# complex(value)
# list(value)
# tuple(value)

# type casting
# value = 12.5
# print(value, type(value))
# value1 = int(value)
# print(value1, type(value1))

# value = 12.5
# print(value)
# value1 = int(value)
# print(value1)

# value = 12 # int
# print(value, type(value))
# value1 = str(value)
# print(value1, type(value1))

# value = 12.5 # float
# print(value, type(value))
# value1 = str(value)
# print(value1, type(value1))

# value = "Hello" # string
# print(value, type(value))
# value1 = list(value)
# print(value1, type(value1))

# value = "Hello" # string
# print(value, type(value))
# value1 = tuple(value)
# print(value1, type(value1))

# value = "Hello" # string
# print(value, type(value))
# value1 = set(value)  # it will not came sequencial
# print(value1, type(value1))

# value = 12
# print(value)
# value1 = complex(value)
# print(value1)

# value = 12
# print(value)
# value1 = complex(value,3)
# print(value1)

# value = 12
# print(value)
# value1 = complex(value,3.5)
# print(value1)

# x = 123
# y = '1.23'

# z = x + float(y)

# print(z)

# Input and Output Function

# Input():- Used to take input from user.

# print():- Used for output on window

# print(object):-

# print(20)
# print(20.5)
# print("dipak")
# print(3+4j)
# print([1,2,3,4,5])

# print(3, 20.5, "dipak", "3+4j", [1,2,3])

# print(3, 20.5, "dipak", "3+4j", [1,2,3], sep='#')
# print("hello")

# pi = 3.14
# print(pi)
# print("value of pi is:", pi)


# print(objects,sep=" ")

# print("hello",20,sep="@")
# print("hello",20,sep="@#")

# print("hello",20,sep="\t")

# print(objects,sep=" ",end="\n")

print("welcome", end=" ")
print("to",end=" ")
print("channel")

# # IF STATMENTS

# num = 10
# if num > 0:
#     print("Positive Number")


# # Control Flow
# # coditional statement - if else elif
# # transfer statement - pass, break, continue
# # # Iterative statement - for, while

# a = 10
# if a == 10:
#     print("ten")
# elif a == 12:
#     print("twelve")
# elif a == "Python":
#     print("Programming Language")
# elif a == [10,20]:
#     print("list")
# else:
#     print("Invalid value")

# a = 10
# if a == 10:
#     print("ten")
# elif a == 12:
#     print("twelve")
# elif a == "Python":
#     print("Programming Language")
# elif a == [10,20]:
#     print("list")
# else:
#     print("Invalid value")

# a = input("Enter a number:- ") # string "10"
# if a == 10:
#     print("ten")
# elif a == 12:
#     print("twelve")
# elif a == "Python":
#     print("Programming Language")
# elif a == [10,20]:
#     print("list")
# else:
#     print("Invalid value")

# a = int(input("Enter a number:- ")) # string "10"
# if a == 10:
#     print("ten")
# elif a == 12:
#     print("twelve")
# elif a == "Python":
#     print("Programming Language")
# elif a == [10,20]:
#     print("list")
# else:
#     print("Invalid value")

# x = 5
# if x > 5:
#     if x % 2 == 0:
#         print("x is greater than 5 and even")
#     else:
#         print("odd")
# else:
#     print("value of x is less than or equal to 5")

# #
# x = 5
# if x > 5:
#     if x % 2 == 0
#         print("x is greater than 5 and even")

# a = None

# if not a: # not None 
#     print("pass")
# else:
#     print("Fail")

# a = ""

# if not a: # not None 
#     print("pass")
# else:
#     print("Fail")

# a = 0

# if not a: # not None 
#     print("pass")
# else:
#     print("Fail")

# # if -- 10 exampke
# # if elif -- 10 example
# # if elif elif else 10 example
# # if and else -- 10 example

# d = {"a": "apple"}
# if "a" in d:
#     print("key is present")

# s = {4,5,2,0,1,5}
# if len(s)!=6:
#     print("pass")


# # bool([]) # False
# # bool("") # False
# # bool(set()) # False
# # bool(None) # False
# # bool(False) # False
# # bool(0) # False
# # bool(" ") # True

# # logical
# # and condition

# a = 10

# if a == 10 and a % 2 == 0:  # TRUE and TRUE = TRUE   1 AND 1 = 1
#     print("The value is 10 and even")

# # OR Condition
# a = 8

# if a == 10 or a % 2 == 0:  # FALSE OR TRUE = TRUE  0 OR 1 = 1
#     print("The value is 10 and even")
# # and


# a = [10,20,30,40,50,"abcd"]

# if (10 in a) and (30 in a) and ("b" in a[5]) and (len(a) == 6) and (a[-1] == "abcd"):
#     print("pass")

# # and

# # 0 0 0
# # 1 0 0
# # 0 1 0 
# # 1 1 1

# # OR

# # 0 0 0
# # 1 0 1
# # 0 1 1
# # 1 1 1

# # not

# # 1 0
# # 0 1
# # True False
# # False True

# fruits = ["apple", "banana", "cherry"]
# fruits.append("mango")
# print(fruits)  
# # Output: ['apple', 'banana', 'cherry', 'mango']
