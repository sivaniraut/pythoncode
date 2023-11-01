"""
The parameter is a listed variable inside of parentheses in the defined function

arguments and parameters  are same

variables are the value we assign to function when we call to it.

There are two type of arguments formal and Actual arguments
"""


def sum(a,b): # This is called Formal Argument
    output = a+b
    print(output)

sum(10,20) # this is called Actual Argument

"""
The actual arguments are four type 
1.Positional Argument
2.keyword Argument
3.default Argument
4. Variablelength Argument 
  a) *args
  b)**kwrgs
  
  Non-keyword arguments (also known as positional arguments) are values 
  passed to a function based on their position in the function call. 
  They match the parameters of the function in the same order
"""

 #Find the area of Rectangle

def area_rectangle(lenth, width):
    """
    :param lenth:(int)
    :param width:int
    :return:multiplication of lenth and width
    """
    area = lenth * width
    return area
area = area_rectangle(5,11)
print(area)

"""
This is called positional Argument here we assign the variable in sequence so it take the input in 
in sequence but what if we don't know the sequence and we will operator the function in some case it will throw 
error we need to used Keyword argument 

keyword argument is nothing but we pass the value with specific parameter name
"""

def area_rectangle(lenth, width):
    """
    :param lenth:
    :param width:
    :return:
    """
    area = lenth * width
    return area
area = area_rectangle(lenth=5,width=9)
print("the total area of rectangle",area)

"""
Defualt Argument Default arguments are values assigned to function parameters in case
the caller of the function doesn't provide a value for those parameters
"""

def person_info(name, age, city="Bangalore"): # default argument
    print(name)
    print(age)
    print(city)


person_info("Sivani",28,)

print("="*80)

"""
Variable length Argument we can define in a function when 
the number of input argument are not fixed. 

we can achieve variable-length arguments using the *args and **kwargs syntax:

"""

#*args = *args collects any number of positional or non keyword arguments into a tuple called args.
# we can pass as many arguments as we want when calling the function

def addition(num, *args):
    total_sum = num
    for i in args:
        total_sum += i
    return total_sum

result = addition(5, 6, 7, 8, 9)# num=5, tupple=(6,7,8,9) we can not add directly
print(result)

print("="*80)

#**kwargs we used it when we want to pass multiple keyword argument

def student_info(name, **personal_details):
    print("Student Name:", name)
    for i,j in personal_details.items():
        print(i, j)

student_info("RAHEEL", age= 10, clas= "4th", rollno = 20)

print("="*80)

def args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for i, j in kwargs.items():
        print(f"{i}: {j}")

args_and_kwargs(1, 2, 3, a=4, b=5)

def test(num1, num2, num3):
    addition = num1 + num2 + num3
    mul = num1 * num2 * num3
    return addition,mul

output = test(1,2,3)
print("output",type(output))





"""
we can use one parameter in different function
"""
def square_num(num):
    result = num ** 2
    return result

def cube_num(num):
    result = num ** 3
    return result

input_num = 4 # this parame

result_square = square_num(input_num)
print("the square of:", input_num, "is", result_square)

result_cube = cube_num(input_num)
print("the cube of:", input_num, "is", result_cube )

print("="*80)

def summation(*args, num):
    total = num
    for i in args:
        total += i
    return total

def multiplication(*given_values, num):
    total = num
    for i in given_values:
        total *= i
    return total

my_num = 10  # Define the common parameter
numbers = (1, 2, 3, 4, 5)

# Calculate the sum and product of numbers using the common parameter
sum_result = summation(*numbers, num=my_num)
product_result = multiplication(*numbers, num=my_num)

print("Sum:", sum_result)
print("Product:", product_result)

print("="*80)

import sys

number = 1234
number1 = number
number2 = number
print("refrance count is", sys.getrefcount(number), id(number))
print("refrance count is", sys.getrefcount(number1), id(number1))
print("refrance count is", sys.getrefcount(number2), id(number2))

"""
we can use an argument as function object 
we can assing variable  to another 
"""

# def addi
# n next step and s step in
#  decorator is special kind of function where it take 1ar function , then difine a inner function and return inner function then inner function have prepossing then innener funcation will call actual then also  we do postprecessing as arrgumeent decotor pressecing before calling the  without change
# we use when we need to check useer valid or not (request validate something)
def test(num1, num2):
    return num1 + num2





