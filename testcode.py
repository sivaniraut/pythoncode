# # # def reverse_str(input_str):
# # #     """
# # #     @Summary: Reverse String
# # #     @Param input_str(str): Input string
# # #     @Return (str): reverse string
# # #     """
# # #     if not isinstance(input_str, str):
# # #         return f"Invalid data type {type(input_str)}"
# # #
# # #     output = ""
# # #     for char in input_str:
# # #         output = char + output
# # #     return output
# # #
# # #
# # # input_data = "ABCDEFG"
# # # result = reverse_str(input_str=input_data)
# # # print("Result:", result)
# #
# #
# # # """
# # # Input: "I am Learning Python"
# # #
# # # Output: "I ma gninraeL nohtyP"
# # #
# # # """
# # #
# # #
# # # def reverse_words01(input_str):
# # #     """
# # #     @Summary: Reverse give wrods from string.
# # #     @Param input_str(str): Input string
# # #     @Retunr (str): String with reverse wrods.
# # #     """
# # #     if not isinstance(input_str, str):
# # #         return "Give input is not str"
# # #     output_str = ""
# # #     word = ""
# # #     for char in input_str:
# # #         if char == " ":
# # #             if output_str:
# # #                 output_str = output_str + " " + word
# # #             else:
# # #                 output_str = word
# # #             word = ""
# # #         else:
# # #             word = char + word
# # #     output_str = output_str + " " + word
# # #     # print("output_str:", output_str, len(output_str))
# # #
# # # input_str = "I am Learning Python"
# # # output_str = reverse_words01(input_str)
# # # print(output_str)
# # #
# #
# #
# # def reverse_words(input_str):
# #     if not isinstance(input_str, str):
# #         return "Input is not a string"
# #
# #     output_string = ""
# #     word = ""
# #
# #     for char in input_str:
# #         if char == " ":
# #             if output_string:
# #                 output_string = output_string + " " + word
# #             else:
# #                 output_string = word
# #             word = ""
# #         else:
# #             word = char + word
# #
# #     output_string = output_string + " " + word
# #     return output_string
# #
# #
# # input_str = "I am Learning Python"
# # output_str = reverse_words(input_str)
# # print(output_str)
# #
# #
# # input_str = "I am Learning Python"
# # reversed_str = ''
# # for char in input_str[::-1]:
# #     reversed_str += char
# # print(reversed_str)
# #
# #
# # def reverse_string(input_str):
# #
# #     if not isinstance(input_str, str):
# #         return f"Invalid data type {type(input_str)}"
# #
# #     output = ""
# #     for char in input_str:
# #         output = char + output
# #     return output
# #
# #
# # input_data = "I am learning python"
# # result = reverse_string(input_str=input_data)
# # print("Result:", result)
#
# def convert_lower_to_upper_upper_to_lower(
#         input_string):
#     """
#     @Summary: Convert Upper to lower case and lower to upper case
#     @Param input_string(str): Input string
#     @Return (str): Output string
#     """
#     if not isinstance(input_string, str):
#         return "Invalid input type, expect only string"
#
#     # A = 65, Z= 65 +25 =90,  a = 97, z = 97 + 25 = 122
#
#     return output_string
#
#
# def convert_list(input_list):
#     """
#     @Summary: Convert List item Upper to lower case and
#     lower to upper case
#     @Param input_list(list): input list
#     @Return (list): Output list
#     """
#     if not isinstance(input_list, list):
#         return "Invalid input type"
#     output_list = []
#     ord_A = ord("A")  # 65
#     ord_Z = ord("Z")
#     ord_a = ord("a")  # 97
#     ord_z = ord("z")
#     for item in input_list:
#         if not isinstance(item, str):
#             print("Invalid item type")
#             # output_list.append(item)
#             continue
#         output_string = ""
#         for char in item:
#             ord_char = ord(char)
#             # Check char is Upper case or not.
#             if ord_char >= ord_A and ord_char <= ord_Z:
#                 new_ord = ord_char + 32
#                 new_char = chr(new_ord)
#                 output_string = output_string + new_char
#             # Check char in Lower case or not.
#             elif ord_char >= ord_a and ord_char <= ord_z:
#                 new_ord = ord_char - 32
#                 new_char = chr(new_ord)
#                 output_string = output_string + new_char
#             else:
#                 output_string = output_string + char
#         output_list.append(output_string)
#     return output_list
#
#
# output = convert_list(
#     ["A b C D", 123, "X y Z", "P Q R"])
# print("output:", output)

# def convert_string(input_string):
#     """
#     @Summary: Convert characters in a string to opposite case
#     @Param input_string(str): Input string
#     @Return (str): Output string
#     """
#     if not isinstance(input_string, str):
#         return "Invalid input type"
#
#     output_string = ""
#     ord_A = ord("A")  # 65
#     ord_Z = ord("Z")
#     ord_a = ord("a")  # 97
#     ord_z = ord("z")
#
#     for char in input_string:
#         ord_char = ord(char)
#         # Check if char is uppercase or not.
#         if ord_char >= ord_A and ord_char <= ord_Z:
#             new_ord = ord_char + 32
#             new_char = chr(new_ord)
#             output_string += new_char
#         # Check if char is lowercase or not.
#         elif ord_char >= ord_a and ord_char <= ord_z:
#             new_ord = ord_char - 32
#             new_char = chr(new_ord)
#             output_string += new_char
#         else:
#             output_string += char
#
#     return output_string
#
#
# output = convert_string("I Am Learning Python")
# print("output:", output)


def shift_characters(input_string):
    """
    @Summary: Shift each character in a string by two places
    @Param input_str(str): Input string
    @Return (str): Output string with shifted characters
    """
    if not isinstance(input_string, str):
        return "Invalid input type"

    shifted_string = ""

    for char in input_string:
        if 'A' <= char <= 'Z':
            shifted_char = chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            shifted_char = chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            shifted_char = char

        shifted_string += shifted_char

    return shifted_string


input_str = "Learn Python"
result = shift_characters(input_str)
print(result)
