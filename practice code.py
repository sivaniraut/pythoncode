# s1 = "()"
# s2 = "(("


# def is_valid_parantheses(s):
#     stack = []
#     for char in s:
#         if char == '(':
#             stack.append()


# def is_valid_string(s):
#     count = 0
#     for char in s:
#         if char =='(':
#             count += 1
#         elif char == ')':
#             count -= 1
#             if count < 0:
#                 return False
#     return count == 0
# s1 = "()"
# s2 = "(("
# s3 = ")("
# s4 = "((()"
# print(is_valid_string(s1))
# print(is_valid_string(s2))
# print(is_valid_string(s3))
# print(is_valid_string(s4))

list1 = [[1,5,6,8,9],"python", 50]
shallowcopy = list(list1)
shallowcopy[0].append(70)
print("shallowcopy:",shallowcopy)
print("normal list:", list1)
print("="*80)
from copy import deepcopy

DL = deepcopy(list1)
DL[0].append(89)
print("deepcopy:", DL)
print("normal list:", list1)
