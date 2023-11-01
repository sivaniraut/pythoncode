# # shallow copy
#
# L = [
#     [1,2, 3,4],
#     "Python",
#     100
# ]
#
# SL = list(L)
# SL[0].append(5)
# print("SL:", SL)
# print("L:", L)
# print("="*80)
# # deep copy
# from copy import deepcopy
#
# DL = deepcopy(L)
# DL[0].append(66)
# print("DL:", DL)
# print("L:", L)


#    0  1   2  3
LL = [3, 2, 6, 4, 9, 19]
# at index 15 at 3rd index
#LL.insert(3, 15)

def insert_item(input_list:list, item: any, index: int=0):
    """
    @summary: insert item at given index
    :param input_list:
    :param item:
    :param index:
    :return:
    """
    # validation
    if not isinstance(input_list, list):
        raise TypeError("invlaid input")
    if not isinstance(index, int):
        raise TypeError("Invlaid index")
    start_index = 0
    len_list = len(input_list)
    while start_index < len_list:
        if start_index == index:
            input_list = input_list[0:index] + [item] + input_list[index:]
            break
        start_index = start_index + 1
    else:
        input_list = input_list + [item]
    return  input_list

LL = [3, 2, 6, 4, 9, 19]
output_list = insert_item(LL, 15, 3)
print("output:", output_list)
# #
#S = {1,2,3, [1,2,3], (1,2,3)}

S = "pipapig"
#madam
# p i p a p i g
long_p = ""
len_s = len(S)
s_list = list(S)
for index in range(len_s):
    pp = ""
    for char in s_list[index:]:
        pp = pp+char
        r_pp = pp[::-1]
        if pp == r_pp:
            if len(long_p) < len(pp):
                long_p = pp
print("long:", long_p)
#
#
#
# Student
# select top 4 from Student order by  desc
# 50
# 40
# 30
# 20  -<< Ans
#
#
# selct top 1 from (select top 4 from Student order by  desc) order by mark asec
# 20
# 30
# 40
# 50
