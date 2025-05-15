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

# Data Types

# numbers
#     - int
#     - float
#     - complex
# sequence
#     - list
#     - tuple
#     - set
#     - frozenset
#     - range
#     - string
#     - bytes
#     - bytearray

# map
#     - dict
# None
# bool -True, False

# # immutable
# # mutable

#   - list
#   - set
#   - bytearray
#   - dictionary

# Let's create examples of all major data types in Python with outputs

# 1. Numeric types: int, float, complex
# numeric_examples = {
#     "int": [10, -5, 0, 999, 1234567890, 42, -100, 1, 7, 200],
#     "float": [10.5, -3.14, 0.0, 999.99, 1e3, -0.001, 3.14159, 2.0, 100.1, 5.5],
#     "complex": [1+2j, -3+4j, 0+0j, 5-2j, 2+0j, -1-1j, 3.14+2.71j, 0+1j, 1j, -1j]
# }

# # 2. Sequence types: str, list, tuple
# sequence_examples = {
#     "str": ["Hello", "Python", "", "123", "abc123", " ", "New\nLine", "Tab\tCharacter", "😀", "Hello World!"],
#     "list": [[1, 2], [], [1, 2, 3], ["a", "b"], [10], list("abc"), [None], [1.1, 2.2], [True, False], [1, "a", 3.0]],
#     "tuple": [(1,), (), (1, 2, 3), ("a",), (1, "b"), tuple("xyz"), (None,), (1.1,), (True, False), (3, "a", 7.8)]
# }

# # 3. Set types: set, frozenset
# set_examples = {
#     "set": [{1, 2, 3}, set(), {10}, {"a", "b"}, {1, 1, 2}, set("abc"), {True, False}, {1.1, 2.2}, {None}, {1, "a", 2.5}],
#     "frozenset": [frozenset({1, 2}), frozenset(), frozenset({10}), frozenset("abc"), frozenset({None}),
#                   frozenset({1.1, 2.2}), frozenset({"a", "b"}), frozenset([1, "a"]), frozenset({True, False}), frozenset("123")]
# }

# # 4. Mapping type: dict
# dict_examples = [
#     {"a": 1}, {}, {"x": 10, "y": 20}, {1: "one", 2: "two"}, {"name": "Alice", "age": 25},
#     dict(a=1, b=2), {"key": None}, {None: "value"}, {"float": 1.1}, {"mixed": [1, 2, 3]}
# ]

# # 5. Boolean type: bool
# bool_examples = [True, False, bool(1), bool(0), bool([]), bool([1]), bool(""), bool("Text"), bool(None), bool(3.14)]

# # 6. Binary types: bytes, bytearray, memoryview
# binary_examples = {
#     "bytes": [b"Hello", bytes(5), b"", bytes([65, 66]), b"123", b"\x00\x01", bytes("abc", "utf-8"), b"A", b"Z", b"\xff"],
#     "bytearray": [bytearray(5), bytearray(b"Hello"), bytearray(), bytearray([1, 2]), bytearray(b"123"), 
#                   bytearray("abc", "utf-8"), bytearray([0, 255]), bytearray(b"A"), bytearray(b"Z"), bytearray(b"\xff")],

# }

"""
welcome
hello
how are you
"""

'''

'''

# output = {
#     "Numeric": numeric_examples,
#     "Sequence": sequence_examples,
#     "Set": set_examples,
#     "Dict": dict_examples,
#     "Boolean": bool_examples,
#     "Binary": binary_examples
# }

# name = "dipak"
# print(type(name))

# age = 27
# print(type(age))

# age = 23.3
# print(type(age))

# age = "s"
# print(type(age))


# age = 2+ 4j
# print(type(age))

# list = [1,2,"dipak", 3+ 4j, True, None]
# print(type(list))

# # isinstance function

# age = 23.3
# print(isinstance(age,int))

# age = 23.3
# print(isinstance(age,int))

# age = 23.3
# result = isinstance(age,int)

# print(result)

# Int

# The int (integer) data type represents whole numbers (no decimals).
# It can be positive, negative, or zero, and has no limit in size.
# It has unlimited length only limited by memory.

# x = 5
# print(x)
# o/p :- class <int>

# print(10)
# print(type(10)) # checking the data type

# create new copy when try to change:-
# x = 5
# #print(x) # 5
# x = 10
# print(x) # 10

# Types of integers:

# Decimal int
# Binary int
# Hexadecimal int
# Octal int

# a = -12
# print(type(a))

# age = 27
# print(type(age))

# num = 120000000000
# print(num)

# print(12,000)
# print(12,5678)

# num1 = 99.99
# print(int(num1))

# num2 = 42
# print(int("42"))

# num = 42
# print(complex(num))

# print(d)

# print(int(True))
# print(True)

# print(int(0b111))

# big_num = 9876543210
# print(big_num)

# h = int(3.2 + 2.7)
# print(h)

# i = int(10 / 3)
# print(i)

# int from string with whitespace
# j = int("  77  ")
# print(j)

# int using underscores for readability
# k = 1_000_000
# print(k)

# Arithmatic Operation

# x = 10
# y = 3
# print(x + y)   # 13
# print(x - y)   # 7
# print(x * y)   # 30
# print(x // y)  # 3 (integer division)
# print(x % y)   # 1 (remainder)
# print(x/y)

# # User defined values
# a = int(input("Enter first number"))
# b = int(input("Enter 2nd number"))
# c = a+b
# print("Total is = ",c)

# a = 10
# b = 5

# c = a+b

# print(c)

# a = 13//3 
# print(a)

# b = -13//3 
# print(b)

# FLOAT

# EX : 97.98 

# int part : 97
# fractional part: 98

# print(float()) # 0.0
# print(float(10)) # 10.0
# print(float("10")) # 10.0
# print(float("10.24")) # 10.24
# print(float("abc")) # value error: could not convert string to float: 'abc'
# print(float("  9  ")) # 9.0
# print(float("  9      \n \n ")) # \n or \t is an escape sequence
# print(float("\f 9 \f"))    
# print(float(1.82e308)) # inf

# Examples of Float() with infinity and NaN

# print(float("infinity"))
# print(float("inf"))
# print(float("nan")) # nan(not a number)
# print(float("NaN"))
      
# print(float("12.33"))
# print(type(10.33))

# print(12.33)
# print(float(10)) # type casting

# num = 97.80
# print(num)
# print(type(num))

# Exponential
# num1 = 2e3
# print(num1)
# print(type(num1))

# salary = 2e3
# print(salary)
# print(type(salary))

# what is float_number.as_integer_ratio()
# syntax: float_number.as_integer_ratio()

# EX : 1
# num = 7.5 # 15/2
# integers = num.as_integer_ratio() # (15,2)
# print(integers)

# EX : 2
# num = 7.5 # 15/2
# a,b = num.as_integer_ratio() # (15,2)
# print(a,b)
# print(a)
# print(b)

# EX : 3
# num = 7.5
# a,b = num.as_integer_ratio() # (15,2)
# print(a,"/",b,'=',num) 15 / 2 = 7.5

# float.is_integer()

# num = 6.8
# print(num.is_integer())

# num = -9.0
# print(num.is_integer())

# num = -9.5
# print(num.is_integer())

# Boolean in Python
# In python, boolean types are represented by the bool class.
# They have two possible values: True and False

# is_married = True
# print(is_married)
# print(type(is_married))

# is_married = False
# print(is_married)
# print(type(is_married))

# non-zero :- True
# zero :- False
# None :- False

# print(bool(10)) # True
# print(bool(0)) # False
# print(bool(-9)) # True
# print(bool(None)) # False

# Empty collection is considered as False
# Non Empty collection is considered as True

# data = []
# data1 = {}
# data2 = ""
# data3 = ()

# print(bool(data))
# print(bool(data1))
# print(bool(data2))
# print(bool(data3))

# True:-
# - non-Zero
# - un-empty collections
# - True
# - an expression returning non-zero Value
# - an expression returning un-empty collections

# False:
# - 0
# - False
# - None
# - empty collections

# name = None
# print(name) # None
# print(type(None)) # <class 'NoneType'>

# COMPLEX DATA TYPE

# # Complex data type written in form of a+bj, a is real part can be int or float and b is an img part can be int or float

# num1 = 3+4j
# print(num1)
# print(type(num2))
# print(num1.real)
# print(num1.imag)

# print(complex()) # oj

# print(complex(1,2)) # (1+2j)

# print(complex(1)) # (1+0j)

# print(complex(1.2)) # (1.2+0j)

# print(complex("a", 2)) # TypeError: complex() can't take second arg if first is a string

# num2 = 2.0+3.2j
# print(type(num2))

# String data type

# string is a sequence of characters. EX. "Shantanu"

# print('Hello World')
# print("Hello World")
# print('''Hello World''')
# print("""Hello World""")
# print(' Hello World')
# print('H')
# print(type('H'))

# print("""
# hello
# wlecome
# back""")

# name = "dipak"
# print(len(name))

# age = "28"
# print(age)
# print(type(age))

# a = "dipakmani"  # if there is no string value present it will showing IndexError: string index out of range
# print(a[5])
# print(a[-12])

# input () gives a string:-
# name = input("enter a name:")
# print(name)

# List
# A list is a collection of values or items of different types.
# Lists are used to store multiple items in a single variable.
# It is a ordered collection
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# List is a collection which is ordered and changeable. Allows duplicate members.

# list = ["Roshan", 20, 40, 30.32, [1,23,45], 2+3j] # index position start with 0
# print(list)
# print(type(list))
# print(list[2])
# list[2]="40.24"
# print(list)

# Indexing in python
# positive / forward indexing start from 0
# negative / reverse indexing start from -1

# list1 = ["Roshan", 20, 40, 30.32, [1,23,45], 2+3j]
# print(type(list1))
# print(list1[0])
# print(list1[1])
# print(list1[-2])


# print(dir(lst))

# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# concatenation of lists

# l1 = [10,20,30,40,30.4,'hello']
# l2 = [40,50,60,'bye']

# print(l1+l2) # [10, 20, 30, 40, 30.4, 'hello', 40, 50, 60, 'bye']
# print(id(l1+l2)) # 2132068890880
# print(id(l1)) # 2132065030144

# Join Two Lists

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# multiplication of list 

# l1 = [10,20,30.4,'hello']
# print(l1*3)

# iteration through list

# l1 = [10,20,30.4,'hello']
# for items in l1:
#     print(items)

# l1 = [10,20,30.4,'hello']
# l2 = [10,20,30,40]
# for items in l2:
#     print(items+1)
#     print(l2)

# membership of list

# l1 = [10,20,30,30.4,"hello"]
# print('hello' in l1)  # True

# l1 = [10,20,30,30.4,"hello"]
# if 'hello' in l1:
#     print("present")
# else:
#     print("not presnt")

# deletion list

# l1 = [10,20,30,30.4,"hello"]
# print(l1)
# del l1
# print(l1)

# length of list
# l1 = [12,12.3,2+3j,'hello',[1,2,3]]
# print("length of list is:",len(l1))

# OR 

# l1 = [12,12.3,2+3j,'hello',[1,2,3]]
# count = 0
# for items in l1:
#     count+=1
# print("length of list is:",count) # o/p is 5 

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1) 

# Maximum in a list

# get largest value in the list
# numbers = [3,2,8,9,10.8,6]
# print(max(numbers))

# get largest ascii string a list
# Name = ['Shantanu','shantan1','Abhijeet','Renuka','Om'] # its consider ascii value of starting value
# print(max(Name))

# A-Z : 65 - 90
# a-z : 97 - 122

# Name = ['Shantanu','shantan1','Abhijeet123','Renuka','Om'] # its consider ascii value of starting value
# print(max(Name,key=len))


# Minimum in a list

# get largest value in the list
# numbers = [3,2,8,9,10.8,6]
# print("minimum value is:",min(numbers))

# Finding the min and max from a list

# nums = [45,78,12,46,53,65,87,91]
# max1=nums[0]
# for ele in nums:
#     if ele>max1:
#         max1=ele
# print("maximum value is:",max1)

# Finding the min and max from a list

# nums = [45,78,12,46,53,65,87,91]
# min1=nums[0]
# for ele in nums:
#     if ele<min1:
#         min1=ele
# print("minimum value is:",min1)

# difference between append and extend

# append() method is used to add a single element to the end of a list.
# This element can be any data type, a number, a string, another list, or even an object.

# a = ['geeks', 'for']

# # Append 'geeks' at the end of 'a'
# a.append('geeks')
# print(a)

# Append an entire list to 'a'
# a.append(['a', 'coding', 'platform'])
# print(a)

# adding multiple items in a list

# bowlers = []
# for i in range(3):
#     name = input("enter name of bowlers:")
#     bowlers.append(name)
# print("bowlers list is:",bowlers)

# extend() Method
# extend() method is used to add all elements from an iterable (e.g., a list, tuple, or set) to the end of the current list. Unlike append(), which adds an entire iterable as a single element,
# extend() adds each element from the iterable to the list.

# a = ['sanket', 'for',6]
# b = [6, 0, 4, 1]

# Add all element of 'b' at the end of 'a'
# a.extend(b)
# print(a)

# append(): Add a single element to the end of the list.
#           It appends an element by modifying list
#           Accept a single element (any data type)
#           Length increases by 1
#           When we want to add one item

# Extend(): Adds multiple elements from an iterable to the end of the list.
#           Accepts an iterable (e.g., list, tuple).
#           Length increases by the number of elements in the iterable.
#           Length increases by the number of elements in the iterable.


# insert method in python

# batsmans = ['rohit','virat','rahul','jadega','hardik']
# batsmans.insert(0,'shaw')
# batsmans.insert(0,'pant')
# batsmans.insert(1,'siraj')

# print(batsmans)


# Remove method

# cart = ['mobile','earphone','laptop','microphone']
# print(cart.remove('laptop'))
# print("updated list is:",cart)

# cart = ['mobile','earphone','laptop','microphone','laptop'] # first remove
# print(cart.remove('laptop'))
# print("updated list is:",cart)

# cart = ['mobile','earphone','laptop','microphone','laptop'] # first remove
# print(cart.remove('pendrive'))
# print("updated list is:",cart)  # ValueError: list.remove(x): x not in list

# cart1 = ['mobile','earphone','laptop','microphone']
# print(cart1.remove())  # TypeError: list.remove() takes exactly one argument (0 given)

# fruits = ['apple', 'banana', 'cherry', 'banana']
# fruits.remove('banana')
# print(fruits)  # ['apple', 'cherry', 'banana']

#  pop(index) – Removes and returns the item at the given index

# numbers = [10, 20, 30, 40]
# print(dir(numbers))
# removed = numbers.pop(2)
# print(numbers)  # [10, 20, 40]
# print(removed)  # 30

# b = [10, 20, 30, 40, 50]
# b.pop()  # removes last
# print(b)  # [10, 20, 30, 40]

# h = []
# h.pop()  # IndexError

# del – Deletes item at a specific index or the entire list

# animals = ['cat', 'dog', 'elephant']
# del animals[1]
# print(animals)  # ['cat', 'elephant']


# del animals[:]  # Deletes all items
# print(animals)  # []


# clear() – Removes all items from the list (makes it empty)

# colors = ['red', 'green', 'blue']
# colors.clear()
# print(colors)  # []

# index()
# lst = [1, 2, 3, 4]
# print(lst.index(3))  # 2

# count()
# lst5 = [1,2,3,4,4,5,5]
# print(lst5.count(5))

# sort()
# unsorted = [3, 1, 4, 2]
# unsorted.sort()
# print(unsorted)  # [1, 2, 3, 4]

# copy()
# copied = lst5.copy()
# print(copied)  # [1, 2, 3, 4, 5, 6]


# my_list = ["India", 20, 20.5, 3+6j, [1, 3, 5], True, None]

# print(my_list)
# print(type(my_list))
# print(my_list[2])
# my_list[2] = "40.5"
# print(my_list)



# tuple 
# Collection of different data types
# immutable, ordered
# Ex. t = (12,12.5,"Hello")

# t = (10,20.4,"hello",[1,2,3])
# print(type(t))
# t[2] = "dipak"
# print(t)


