#  decorator is special kind of function where it take 1ar
#  function , then difine a inner function and return inner
#  function then inner function have prepossing then innener
#  funcation will call actual then also  we do postprecessing as arrgumeent
#  decotor pressecing before calling the  without change
# we use when we need to check useer valid or not (request validate something)
"""
decorator is a special kind of function where it takes first function as an argument then its diffine inner function and
its return inner function logic as function.

decorators specify by @name_of_function, we use it to modify a function without
enhancing the function code

"""

import time


def calucate_time(func, *args, **kwargs):
    """

    :param func:
    :param args:
    :param kwargs:
    :return:
    """

    start_time = time.time()
    output = func(*args, **kwargs)
    end_time = time.time()
    time_taken = end_time - start_time
    print("Time taken by func {}, seconds - {}".format(func, time_taken))
    return output

def addition1(num1, num2):
    time.sleep(5)
    return num1 + num2

def addition2(num1, num2, num3):
    time.sleep(6)
    return num1 + num2 + num3

output = calucate_time(addition1, 20,90)
print("addition1 output:", output)

output = calucate_time(addition2,10, 20, 40)
print("addition2 output:", output)

print("=" * 80)

def calculate_time(func):
    print("I am at start of calculate time")
    def inner(*args,**kwargs):
        print("i m at start of inner function")
        start_time = time.time()
        output = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print("Time taken by func {}, seconds: {}".format(func.__name__, total_time))
        print("i m end of function")
        return output
    print("i m end of calculate time")
    return inner # the inner function will return the return value of actual function



@calculate_time
def add1(number1, number2):
    time.sleep(2)
    return number1 + number2

@calculate_time
def add2(num1, num2, num3):
    time.sleep(3)
    return num1 + num2 + num3

output = add1(5, 6)
print("1st addition:", output)

output = add2(8, 9, 10)
print("2nd addition:", output)

print("=" * 80)

def decorater1(num):
    def inner(*args, **kwargs):
        a = num()
        multi = a * 5
        return multi
    return inner

def decorater2(num):
    def inner(*args, **kwargs):
        b = num()
        add = b + 5
        return add
    return inner

@decorater2
@decorater1
def num():
    return 10

# num = decorater2(decorater1(num))
print(num())

"""
we can also use the two decorator on one function 
"""






