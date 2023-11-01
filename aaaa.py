
INPUT_LIST = [1, 4, 5, 7, 8, 9, 3, 12, 3, 7, 1]
# 1, 4, 5, 7, 8, 9, 3, 12, 3, 7, 1
# 

def find_first_repeated(input_list: list):
    """doctsting"""
    output = ""
    number_list = []
    for i in input_list:
        if i in number_list:
            print(i)
            break
        else:
            number_list.append(i)



    for index in range(len(input_list)):
        new_list = input_list[index:]
        first_number = new_list[0]  # 1
        number_list = []
        for i in new_list[1:]:  # 4,5,7,8,9,3,12,3,7,1
            if first_number == i:  # 4, 5, 7, 8,  9, 3 , 12 ,3
                output = first_number
                break
            if i in number_list:  # 4,5,7,8,9,3,12,
                break
            number_list.append(i)  #
        if output:
            break
    if output:
        print("output:", output)

find_first_repeated(INPUT_LIST)




