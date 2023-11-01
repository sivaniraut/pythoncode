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
import pdb


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


output = add1(5, 6)
print("1st addition:", output)
