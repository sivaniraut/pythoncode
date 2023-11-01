import os

def report_file_line(input_file_path):
    if not os.path.isfile(input_file_path):

        raise ValueError("File not found")

    with open(input_file_path, "r") as fp:
        data = fp.read()
        no_lines = data.count("\n")
        report = f"Number of lines: {no_lines}"
        return report

input_file_path = "C:\\Users\DELL\PycharmProjects\pythonProject\\test.txt"
report = report_file_line(input_file_path)

print(report)

print("="*80)

def report_char(input_file_path):
    if not os.path.isfile(input_file_path):
        raise ValueError("File not found")

    with open(input_file_path, "r") as fp:
        data = fp.read()
        total_characters = len(data)
        return total_characters

input_file_path = "C:\\Users\DELL\PycharmProjects\pythonProject\\test.txt"
total_characters = report_char(input_file_path)

print(f"Total characters: {total_characters}")

print("="* 80)

def count_spaces(input_file_path):
    """
    Count the total number of spaces in a text file
    Raises:ValueError: If the file does not exist.
    :param input_file_path:
    :return: no of spaces
    """
    if not os.path.isfile(input_file_path):
        raise ValueError("File not found")

    with open(input_file_path, "r") as fp:
        data = fp.read()
        total_spaces = data.count(" ")
        return total_spaces

input_file_path = "C:\\Users\DELL\PycharmProjects\pythonProject\\test.txt"
total_spaces = count_spaces(input_file_path)

print(f"Total spaces: {total_spaces}")


print("="* 80)



def CountCapitalLetter(input_file_path: str):
    """Count the number of capital letters in a text file."""

    # Check if the file exists
    if not os.path.isfile(input_file_path):
        raise ValueError("File not found")  # Fix the typo in the error message

    # Open the file and read its content
    fp = open(input_file_path, "r")
    data = fp.read()

    capital_letter_counter = 0
    ord_A = ord("A")  # ASCII code for 'A' is 65
    ord_Z = ord("Z")  # ASCII code for 'Z' is 90


    for char in data:
        char_ord = ord(char)
        if ord_A <= char_ord <= ord_Z:
            capital_letter_counter += 1

    return capital_letter_counter


FILE_PATH = "C:\\Users\\DELL\\PycharmProjects\\pythonProject\\test.txt"
output = CountCapitalLetter(FILE_PATH)
print("output:", output)

print("="*80)



def count_small_letters(input_file_path: str):
    """Count the number of small letters in a text file."""

    if not os.path.isfile(input_file_path):
        raise ValueError("File not found")

    with open(input_file_path, "r") as fp:
        data = fp.read()

    small_letter_counter = 0
    ord_a = ord("a")  # ASCII code for 'a' is 97
    ord_z = ord("z")  # ASCII code for 'z' is 122

    for char in data:
        char_ord = ord(char)
        if ord_a <= char_ord <= ord_z:
            small_letter_counter += 1

    return small_letter_counter


FILE_PATH = "C:\\Users\\DELL\\PycharmProjects\\pythonProject\\test.txt"
output = count_small_letters(FILE_PATH)
print("output:", output)

print("="*80)


def count_total_digits(input_file_path: str):
    """Count the total number of digits (0-9) in a text file."""

    if not os.path.isfile(input_file_path):
        raise ValueError("File not found")

    with open(input_file_path, "r") as fp:
        data = fp.read()

    total_digit_count = 0

    for char in data:
        if char.isdigit():
            total_digit_count += 1

    return total_digit_count


FILE_PATH = "C:\\Users\\DELL\\PycharmProjects\\pythonProject\\test.txt"
output = count_total_digits(FILE_PATH)
print("Total digit count:", output)


