# Input: ABCDEFG
#
# OUTPUT: GFEDCBA
#
# A
# ""          "A"
# B
# "A"         "B" + "A" = "BA"
# C
# "BA"        "C" + "BA" = "CBA"
# D
# "CBA"       "D" + "CBA" = "DCBA"
#
# Input: "I am Learning Python"
#
# Output: "I ma gninraeL nohtyP"
#
# """
#
# def reverse_str(input_str):
#     """
#
#
# @Summary
#
# : Reverse
# String
#
#
# @Param
#
#
# input_str(str): Input
# string
#
#
# @Return(str)
#
# : reverse
# string
# """
# if not isinstance(input_str, str):
#     return f"Invalid data type {type(input_str)}"
#
# output = ""
# for char in input_str:
#     output = char + output
# return output
#
#
# input_data = "ABCDEFG"
# result = reverse_str(input_str=input_data)
# print("Result:", result)


def revers_string(input_str):
    if not isinstance(input_str,str):
        return f"invaild data type{type(input_str)}"
    output = ""
    for char in input_str:
        output = char + output
    return output

input_data = "hello sivani "
result = revers_string(input_str=input_data)
print("Result:", result)