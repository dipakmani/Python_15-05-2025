# Introduction
# Day 1 

# print(3 + 2)   # addition(+)
# print(3 - 2)   # subtraction(-)
# print(3 * 2)   # multiplication(*)
# print(3 / 2)   # division(/)
# print(3 ** 2)  # exponential(**)
# print(3 % 2)   # modulus(%)
# print(3 // 2)  # Floor division operator(//)

# # Checking data types

# print(type(10))                  # Int
# print(type(3.14))                # Float
# print(type(1 + 3j))              # Complex
# print(type('Asabeneh'))          # String
# print(type([1, 2, 3]))           # List
# print(type({'name':'Asabeneh'})) # Dictionary
# print(type({9.8, 3.14, 2.7}))    # Set
# print(type((9.8, 3.14, 2.7)))    # Tuple
# print(type(3 == 3))              # Bool
# print(type(3 >= 3))              # Bool



# # Day 2 Variables in Python

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# country = 'Finland'
# city = 'Helsinki'
# age = 250
# is_married = True
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#     'firstname':'Asabeneh', 
#     'lastname':'Yetayeh', 
#     'country':'Finland',
#     'city':'Helsinki'
#     }

# # Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

# # Declaring multiple variables in one line

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)


# # Day 3 Arithmetic Operations in Python
# # Integers

# print('Addition: ', 1 + 2)
# print('Subtraction: ', 2 - 1)
# print('Multiplication: ', 2 * 3)
# print ('Division: ', 4 / 2)                         # Division in python gives floating number
# print('Division: ', 6 / 2)
# print('Division: ', 7 / 2)
# print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
# print('Modulus: ', 3 % 2)                           # Gives the remainder
# print ('Division without the remainder: ', 7 // 3)
# print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# # Floating numbers
# print('Floating Number,PI', 3.14)
# print('Floating Number, gravity', 9.81)

# # Complex numbers
# print('Complex number: ', 1 + 1j)
# print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# # Declaring the variable at the top first

# a = 3 # a is a variable name and 3 is an integer data type
# b = 2 # b is a variable name and 3 is an integer data type

# # Arithmetic operations and assigning the result to a variable
# total = a + b
# diff = a - b
# product = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponential = a ** b

# # I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
# print(total) # if you don't label your print with some string, you never know from where is  the result is coming
# print('a + b = ', total)
# print('a - b = ', diff)
# print('a * b = ', product)
# print('a / b = ', division)
# print('a % b = ', remainder)
# print('a // b = ', floor_division)
# print('a ** b = ', exponential)

# # Declaring values and organizing them together
# num_one = 3
# num_two = 4

# # Arithmetic operations
# total = num_one + num_two
# diff = num_two - num_one
# product = num_one * num_two
# div = num_two / num_two
# remainder = num_two % num_one

# # Printing values with label
# print('total: ', total)
# print('difference: ', diff)
# print('product: ', product)
# print('division: ', div)
# print('remainder: ', remainder)


# # Calculating area of a circle
# radius = 10                                 # radius of a circle
# area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
# print('Area of a circle:', area_of_circle)

# # Calculating area of a rectangle
# length = 10
# width = 20
# area_of_rectangle = length * width
# print('Area of rectangle:', area_of_rectangle)

# # Calculating a weight of an object
# mass = 75
# gravity = 9.81
# weight = mass * gravity
# print(weight, 'N')

# print(3 > 2)     # True, because 3 is greater than 2
# print(3 >= 2)    # True, because 3 is greater than 2
# print(3 < 2)     # False,  because 3 is greater than 2
# print(2 < 3)     # True, because 2 is less than 3
# print(2 <= 3)    # True, because 2 is less than 3
# print(3 == 2)    # False, because 3 is not equal to 2
# print(3 != 2)    # True, because 3 is not equal to 2
# print(len('mango') == len('avocado'))  # False
# print(len('mango') != len('avocado'))  # True
# print(len('mango') < len('avocado'))   # True
# print(len('milk') != len('meat'))      # False
# print(len('milk') == len('meat'))      # True
# print(len('tomato') == len('potato'))  # True
# print(len('python') > len('dragon'))   # False

# # Boolean comparison
# print('True == True: ', True == True)
# print('True == False: ', True == False)
# print('False == False:', False == False)
# print('True and True: ', True and True)
# print('True or False:', True or False)

# # Another way comparison 
# print('1 is 1', 1 is 1)                   # True - because the data values are the same
# print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
# print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
# print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
# print('coding' in 'coding for all') # True - because coding for all has the word coding
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# print(3 > 2 and 4 > 3) # True - because both statements are true
# print(3 > 2 and 4 < 3) # False - because the second statement is false
# print(3 < 2 and 4 < 3) # False - because both statements are false
# print(3 > 2 or 4 > 3)  # True - because both statements are true
# print(3 > 2 or 4 < 3)  # True - because one of the statement is true
# print(3 < 2 or 4 < 3)  # False - because both statements are false
# print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
# print(not True)      # False - Negation, the not operator turns true to false
# print(not False)     # True
# print(not not True)  # True
# print(not not False) # False

# # Day 4

# # Single line comment
# letter = 'P'                # A string could be a single character or a bunch of texts
# print(letter)               # P
# print(len(letter))          # 1
# greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
# print(greeting)             # Hello, World!
# print(len(greeting))        # 13
# sentence = "I hope you are enjoying 30 days of python challenge"
# print(sentence)

# # Multiline String
# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)
# # Another way of doing the same thing
# multiline_string = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string)

# # String Concatenation
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# space = ' '
# full_name = first_name  +  space + last_name
# print(full_name) # Asabeneh Yetayeh
# # Checking length of a string using len() builtin function
# print(len(first_name))  # 8
# print(len(last_name))   # 7
# print(len(first_name) > len(last_name)) # True
# print(len(full_name)) # 15

# #### Unpacking characters 
# language = 'Python'
# a,b,c,d,e,f = language # unpacking sequence characters into variables
# print(a) # P
# print(b) # y
# print(c) # t 
# print(d) # h
# print(e) # o
# print(f) # n

# # Accessing characters in strings by index
# language = 'Python'
# first_letter = language[0]
# print(first_letter) # P
# second_letter = language[1]
# print(second_letter) # y
# last_index = len(language) - 1
# last_letter = language[last_index]
# print(last_letter) # n

# # If we want to start from right end we can use negative indexing. -1 is the last index
# language = 'Python'
# last_letter = language[-1]
# print(last_letter) # n
# second_last = language[-2]
# print(second_last) # o

# # Slicing

# language = 'Python'
# first_three = language[0:3] # starts at zero index and up to 3 but not include 3
# last_three = language[3:6]
# print(last_three) # hon
# # Another way
# last_three = language[-3:]
# print(last_three)   # hon
# last_three = language[3:]
# print(last_three)   # hon

# # Skipping character while splitting Python strings
# language = 'Python'
# pto = language[0:6:2] # 
# print(pto) # pto

# # Escape sequence
# print('I hope every one enjoying the python challenge.\nDo you ?') # line break
# print('Days\tTopics\tExercises')
# print('Day 1\t3\t5')
# print('Day 2\t3\t5')
# print('Day 3\t3\t5')
# print('Day 4\t3\t5')
# print('This is a back slash  symbol (\\)') # To write a back slash
# print('In every programming language it starts with \"Hello, World!\"')

# ## String Methods
# # capitalize(): Converts the first character the string to Capital Letter

# challenge = 'thirty days of python'
# print(challenge.capitalize()) # 'Thirty days of python'

# # count(): returns occurrences of substring in string, count(substring, start=.., end=..)

# challenge = 'thirty days of python'
# print(challenge.count('y')) # 3
# print(challenge.count('y', 7, 14)) # 1
# print(challenge.count('th')) # 2`

# # endswith(): Checks if a string ends with a specified ending

# challenge = 'thirty days of python'
# print(challenge.endswith('on'))   # True
# print(challenge.endswith('tion')) # False

# # expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

# challenge = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs())   # 'thirty  days    of      python'
# print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# # find(): Returns the index of first occurrence of substring

# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0

# # format()	formats string into nicer output    
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# job = 'teacher'
# country = 'Finland'
# sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
# print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

# radius = 10
# pi = 3.14
# area = pi # radius ## 2
# result = 'The area of circle with {} is {}'.format(str(radius), str(area))
# print(result) # The area of circle with 10 is 314.0

# # index(): Returns the index of substring
# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0

# # isalnum(): Checks alphanumeric character

# challenge = 'ThirtyDaysPython'
# print(challenge.isalnum()) # True

# challenge = '30DaysPython'
# print(challenge.isalnum()) # True

# challenge = 'thirty days of python'
# print(challenge.isalnum()) # False

# challenge = 'thirty days of python 2019'
# print(challenge.isalnum()) # False

# # isalpha(): Checks if all characters are alphabets

# challenge = 'thirty days of python'
# print(challenge.isalpha()) # True
# num = '123'
# print(num.isalpha())      # False

# # isdecimal(): Checks Decimal Characters

# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0

# # isdigit(): Checks Digit Characters

# challenge = 'Thirty'
# print(challenge.isdigit()) # False
# challenge = '30'
# print(challenge.digit())   # True

# # isdecimal():Checks decimal characters

# num = '10'
# print(num.isdecimal()) # True
# num = '10.5'
# print(num.isdecimal()) # False


# # isidentifier():Checks for valid identifier means it check if a string is a valid variable name

# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True


# # islower():Checks if all alphabets in a string are lowercase

# challenge = 'thirty days of python'
# print(challenge.islower()) # True
# challenge = 'Thirty days of python'
# print(challenge.islower()) # False

# # isupper(): returns if all characters are uppercase characters

# challenge = 'thirty days of python'
# print(challenge.isupper()) #  False
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper()) # True


# # isnumeric():Checks numeric characters

# num = '10'
# print(num.isnumeric())      # True
# print('ten'.isnumeric())    # False

# # join(): Returns a concatenated string

# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = '#, '.join(web_tech)
# print(result) # 'HTML# CSS# JavaScript# React'

# # strip(): Removes both leading and trailing characters

# challenge = ' thirty days of python '
# print(challenge.strip('y')) # 5

# # replace(): Replaces substring inside

# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# # split():Splits String from Left

# challenge = 'thirty days of python'
# print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# # title(): Returns a Title Cased String

# challenge = 'thirty days of python'
# print(challenge.title()) # Thirty Days Of Python

# # swapcase(): Checks if String Starts with the Specified String
  
# challenge = 'thirty days of python'
# print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
# challenge = 'Thirty Days Of Python'
# print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# # startswith(): Checks if String Starts with the Specified String

# challenge = 'thirty days of python'
# print(challenge.startswith('thirty')) # True
# challenge = '30 days of python'
# print(challenge.startswith('thirty')) # False


# Day 5

# empty_list = list() # this is an empty list, no item in the list
# print(len(empty_list)) # 0

# fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# # Print the lists and it length
# print('Fruits:', fruits)

# print('Number of fruits:', len(fruits))
# print('Vegetables:', vegetables)
# print('Number of vegetables:', len(vegetables))
# print('Animal products:',animal_products)
# print('Number of animal products:', len(animal_products))
# print('Web technologies:', web_techs)
# print('Number of web technologies:', len(web_techs))
# print('Number of countries:', len(countries))

# Modifying list

# fruits = ['banana', 'orange', 'mango', 'lemon'] 
# first_fruit = fruits[0] # we are accessing the first item using its index
# print(first_fruit)      # banana
# second_fruit = fruits[1]
# print(second_fruit)     # orange
# last_fruit = fruits[3]
# print(last_fruit) # lemon
# # Last index
# last_index = len(fruits) - 1
# last_fruit = fruits[last_index]


# fruits = ['banana', 'orange', 'mango', 'lemon']    # 'banana'
# first_char = fruits[0][1]   # 'b'
# print(first_char)


# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]


# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]


# fruits = ['banana', 'orange', 'mango', 'lemon'] 
# fruits[0] = 'Avocado' 
# print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
# fruits[1] = 'apple'
# print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
# last_index = len(fruits) - 1
# fruits[last_index] = 'lime'
# print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# # checking items
# fruits = ['banana', 'orange', 'mango', 'lemon']
# does_exist = 'banana' in fruits
# print(does_exist)  # True
# does_exist = 'lime' in fruits
# print(does_exist)  # False