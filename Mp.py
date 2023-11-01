"""File opne"""

class CustomContextManager:
    def __init__(self, filename, mode="r"):
        self.filename =filename

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



def test(func):
    def inner(*args, **kwargs):
        print("Preprocessing")
        output = func(args, kwargs)
        print("Postprocsiing")

    return inner()


L = [1, 23, 3, 4, 55, 0]

def incremental_sequence(input_list: list) -> list:
    """Docstinrg"""

    output = [input_list[0]]
    longext_list = []
    prev_num = input_list[0]
    for num in input_list[1:]:
        if prev_num is None:
            prev_num = num
            output = [num]
        elif num > prev_num:
            prev_num = num
            output.append(num)
        else:
            if len(longext_list) < len(output):
                longext_list = output
            output = []
            prev_num = None
    return longext_list

response = incremental_sequence(L)
print("resp:", response)
exit(0)
if L[0] > L[1]:
    largest_number = L[0]
    second_largest = L[1]
else:
    largest_number = L[1]
    second_largest = L[0]

for num in L[2:]:
    if num > largest_number:
        second_largest = largest_number
        largest_number = num
    elif num > second_largest:
        second_largest = num

print("Second:", second_largest)

"""
customer DB
    customer name
    cust id
    dob
    address

store DB
    cust_id
    product_id
    product_quent
    purs_amount

Product DB
    product_id
    product_name
    product_availability
    product_cost
    
Select Customer.customer_name,  from store_db
Customer where customer_name like "a%"
Select id from Product where product_name 

"""

