add_5 = lambda a, b: a + b + 5

output = add_5(10, 20)

#Capital letter
import os

def CountCapitalLetter(input_file_path: str):
    """docstring"""

    if not os.path.isfile(input_file_path):
        raise ValueError("Not prrsent")

    fp = open(input_file_path, "r")
    data = fp.read()
    capital_latter_counter = 0
    ord_A = ord("A") # A =65
    ord_Z = ord("Z")
    for char in data:
        char_ord  = ord(char)
        if char_ord >= ord_A and char_ord <= ord_Z:
            capital_latter_counter = capital_latter_counter + 1

    return capital_latter_counter

FILE_PATH = "C:\\Users\DELL\PycharmProjects\pythonProject\\test.txt"
output = CountCapitalLetter(FILE_PATH)
print("output:", output)

# 1. Read logs files.
# 2. logs format -> fetch data
# 3.

# two file
# Reports - number

def rpeort_file(input_file_path):

    if not os.path.isfile(input_file_path):
        raise ValueError("Not prrsent")

    fp = open(input_file_path, "r")
    data = fp.read()
    no_lines = data.count("\n")
    no_spaces = data.count(" ")
    total_char = len(data)
    report = {
        "number_of_lines": no_lines,
        "number_of_spaces": no_spaces,
        "total_characters": total_char
    }
    return report

FILE_PATH = "C:\\Users\DELL\PycharmProjects\pythonProject\\test.txt"
report_file_01 = rpeort_file(FILE_PATH)
FILE_PATH_02 = "C:\\Users\DELL\PycharmProjects\pythonProject\\test2.txt"
report_file_02 = rpeort_file(FILE_PATH_02)
print("output:", report_file_01, "\n", report_file_02)

def rpeort_file(input_file_path01, input_file_path02):

    if not os.path.isfile(input_file_path01):
        raise ValueError("Not prrsent")

    if not os.path.isfile(input_file_path02):
        raise ValueError("File not presnt")

    fp = open(input_file_path01, "r")
    data01 = fp.read()
    fp.close()
    fp = open(input_file_path02, "r")
    data02 = fp.read()
    fp.close()

    words01 = data01.split(" ")
    words02 = data02.split(" ")

    for wd in words01:
        if wd not in words02:
            print(f"{wd} from file 01 not present in file 02")


    for wd in words02:
        if wd not in words01:
            print(f"{wd} from file 02 not present in file 01")

rpeort_file(FILE_PATH, FILE_PATH_02)

