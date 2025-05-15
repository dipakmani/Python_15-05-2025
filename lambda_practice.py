# def func1(var, var1):
#     return var+var1

# def func2(num):
#     return num ** 2
# print(func2(20))

# def func(*args):
#     print(sum(args))

# func(1,2,3,4)

# basic syntax of lambda

# lambda arguments: expression

# 1. Lambda with Positional Arguments
# Takes 2 arguments and returns there sum

# add = lambda x, y: x + y
# print(add(5+3))


# res = lambda *args: print(sum(args))
# res(1,2,3,4)


# res = lambda var, var1: var+var1
# print(res(10,20))

# res = lambda num: num ** 2  # we didn't gave the name is called as ananymous function
# print(res)
# print(res(5))


# higher order function
# map, filter, reduce

def square(num):
    return num ** 3

res = list(map(square, [1,2,3,4,5]))
print(res)

# map = har ek ke paas jana
# filter : kisi chis ko filter krna
# reduce : kam karna list mai se value ka addition krna to