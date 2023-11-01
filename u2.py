lst = ["P", "Y", "T", "H", "O", "N"]

output = "".join(lst)
print("output:", output)

"""
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

 

Suppose the following input is supplied to the program:

 

8

 

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""


def generate_seq_dict(end_no, start_no=1):
    """docsting"""

    if not isinstance(end_no, int):
        raise ValueError("invalid value")

    output = {}
    counter = start_no
    while counter <= end_no:
        output[counter] = counter * counter
        counter = counter + 1

    return output

end_no = -5

#response = generate_seq_dict(end_no)
#print("response:", response)


string = "P r ogramm in g "

print("number of spaces:", string.count(" "))


import sys
import os
args = sys.argv
print("args:", args)
#file_path = args[1]
#word = args[2]

def search_word(file_path, word):
    """"""
    if not os.path.isfile(file_path):
        raise ValueError("File not present")
    counter = 0
    fp = open(file_path, "r")
    lines = fp.readlines()
    for line in lines:
        if word in line:
            print("Line:", line)
            counter = counter + 1
    print("Total words found:", counter)

#search_word(file_path, word)


class Parent:
    def test(self):
        print("I am test from parent")

class Child(Parent):
    def test(self):
        super().test()
        print("I am overloading test method of prent class")

obj= Child()
obj.test()


