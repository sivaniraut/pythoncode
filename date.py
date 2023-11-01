

class Date:
    """ Day / month/ year"""


    def __init__(self, day, momth, year) -> None:
        self.dd = day
        self.mm = momth
        self.yy = year

    def get_date(self):
        return "{}/{}/{}".format(
            self.dd, self.mm, self.yy)

    def set_date(self, input_dd: int, input_mm: int, input_yy: int) -> None:
        """
        @Summary: Set date.
        """
        # validate - 1. type of parameters, 2. value check
        if not isinstance(input_dd, int):
            raise ValueError(f"Invalid type {type(input_dd)} for input_dd")
        if not isinstance(input_mm, int):
            raise ValueError(f"Invalid type {type(input_mm)} for input_mm")
        if not isinstance(input_yy, int):
            raise ValueError(f"Invalid type {type(input_yy)} for input_yy")
        # Value check
        # DD - 1 to 31
        if input_dd >= 1 and input_dd <= 31:
            self.dd = input_dd
        else:
            raise ValueError(f"Invalid value {input_dd} for input_dd, it should be in between 1 to 31")
        # MM
        if input_mm >= 1 and input_mm <= 12:
            self.mm = input_mm
        else:
            raise ValueError(f"Invlaid value {input_mm} for input_mm, it shoul be in between 1 to 12")
        # year
        if input_yy >= 2000 and input_yy <= 2999:
            self.yy = input_yy
        else:
            raise ValueError(f"invalid value {input_yy} for year, it shout be between 2000 and 2999")

    def year_diff(self, obj2) -> int:
        """
        year differance bewtween two date object
        """
        print("self: ", id(self))
        print("obj2: ", id(obj2))
        print(self.yy, obj2.yy)

    # def year_mm()


sample_date = Date(10, 7, 2023)
print("Sample Date:", sample_date.get_date())
print("Sample Date:", Date.get_date(sample_date))
# sample_date.get_date()  => Date.get_date(sample_date)

print("set new date to existing object/instance")
sample_date.set_date(30, 12, 2018)
print("Sample Date1:", sample_date.get_date())

sample_date2 = Date(10, 7, 2023)
print("Sample Date2:", sample_date2.get_date())

print("sample_date1: ", id(sample_date))
print("sample_date2: ", id(sample_date2))

sample_date2.year_diff(sample_date)  # Date.year_diff(sample_date2, sample_date)

# differance between months

"""
1/1/2023  10/7/2023 
 >> 6 months

1/1/2023   10/7/2024
>> 1/1/2023 to 31/12/2023  -> 11 months 
    31/12/2023 to 10/7/2024  -> 7 months

    18 moths

"""
"""
Credit Card:
    Card Number : 16 digit number
    Expiration Date: Month/Year
    CardHolder Name: Frist name Last Name
    CVC Number: 3 digit number
"""


class CreditCard:
    def __init__(
            self, card_num, expiration_date, name, cvc_num):
        self.card_num = card_num
        self.expiration_date = expiration_date
        self.cardholder_name = name
        self.cvc_num = cvc_num

    def __str__(self, ):
        print("in str method")
        return f"Card Num: {self.card_num}, Name:{self.cardholder_name}"

    # obj1 = CreditCard(
    #     "1234567890123456",
    #     "05/25",
    #     "Vivek Sable",
    #     123
    # )