# if-else in python:

# Python's if...else is used to control the flow of execution based on conditions.

# if condition:
#     # block if condition is True
# elif another_condition:
#     # block if this condition is True
# else:
#     # block if none of the above are True

# 01 Check if list is empty
# my_list = []
# if my_list:
#     print("List is not empty")
# else:
#     print("List is empty")

# 02 Check if a value exists in list
# my_list = [1,2,4,6]
# if 2 in my_list:
#     print("2 is in the list")
# else:
#     print("2 is not in rhe list")

# 03 Compare lengths of two lists
# a = [1,2]
# b = [3,4,5]
# if len(a) > len(b):
#     print("List a is longer")
# else:
#     print("List b is longer or equal")

# 04 Check if list contains only even numbers
# nums = [2, 4, 6]
# if nums % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd number")

# num = int(input("Enter a number:"))
# if nums % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd number")


# nums = int(input("Enter a number:"))
# if nums > 0:
#     print("Number is Positive")
# else:
#     print("Number is Negative")

# nums = [2, 5, 6]
# if sum(nums) > 10:
#     print("Sum is greater than 10")
# else:
#     print("Sum is 10 or less")
# else:
#     print("ok")


# # 1)
# air_quality = 180
# if air_quality < 100:
#     print("Air quality is good")
# else:
#     print("Air quality is bad")

# # 2)
# pH_level = 7
# if 6.5 <= pH_level <=8.5:
#     print("Water is safe for drink")
# else: print("Water is not safe")

# # 3)
# rainfall = 200
# if rainfall < 300:
#     print("The city is facing a drought")
# else:
#     print("The city has sufficient water")

# # 4)
# protected_forests = ["Amazon","Sundarbans"]
# forest = "Amazon"
# if forest in protected_forests:
#     print("This is a protected forest")

# # 6)

# segregation = True
# if segregation:
#     print("The city follows waste segregation")
# else:
#     print("The city does not follow waste segregation")

# # 7) 
# temperature = 101
# if temperature > 100:
#     print("Patient has a fever")
# else:
#     print("Normal temperature")


# # 8
# num = -10
# if num > 0:
#     print("Positive")
# else:
#     print("Negative")

# # 9. Check if a string is uppercase

# word = "HELLO"
# if word.isupper():
#     print("Uppercase")
# else:
#     print("Not uppercase")

# # 10. Check if a year is a leap year
# year = 2024
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")    

# # 11
# age = 17
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# # 12
# password = "abcd123"
# if len(password) >= 8:
#     print("Strong password")
# else:
#     print("Weak password")

# # 13
# email = "example.com"
# if "@" in email:
#     print("Valid email")
# else:
#     print("Invalid email")

# # 14
# num = 9
# if num % 3 == 0:
#     print("Divisible by 3")
# else:
#     print("Not divisible by 3")

# # 15
# value = "123"
# if value.isnumeric():
#     print("Numeric")
# else:
#     print("Not numeric")

# # 16
# value = "qwe123"
# if value.isalnum():
#     print("AlphaNumeric")
# else:
#     print("Not AlphaNumeric")

# # 17
# is_active = False
# if is_active:
#     print("User is active")
# else:
#     print("User is inactive")

# # 18
# length, width = 5, 10
# if length == width:
#     print("Square")
#     print("Square")
# else:
#     print("Rectangle")
#     print("Rectangle")

# # 19
# location = "Wild"
# if location == "Zoo":
#     print("Animal is in captivity")
# else:
#     print("Animal is in the wild")

# # 20
# resource = "Natural Gas"
# if resource in ["Solar", "Wind", "Hydro"]:
#     print(f"{resource} is a renewable resource")
# else:
#     print(f"{resource} is a non-renewable resource")

# # 21
# char = 'e'
# if char in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")

# # 22
# a = 20
# if a % 2 == 0:
#     print("even number")
# else:
#     print("odd number")