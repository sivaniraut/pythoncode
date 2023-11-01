class Date:
    """ Day / month / year"""

    def __init__(self, day, month, year):
        self.dd = day
        self.mm = month
        self.yy = year

    def get_date(self):
        return f"{self.dd}/{self.mm}/{self.yy}"

    def set_date(self, input_dd, input_mm, input_yy):
        # Validate input types
        if not isinstance(input_dd, int):
            raise ValueError(f"Invalid type {type(input_dd)} for input_dd")
        if not isinstance(input_mm, int):
            raise ValueError(f"Invalid type {type(input_mm)} for input_mm")
        if not isinstance(input_yy, int):
            raise ValueError(f"Invalid type {type(input_yy)} for input_yy")

        # Validate input values
        if input_dd < 1 or input_dd > 31:
            raise ValueError(f"Invalid value {input_dd} for input_dd, it should be between 1 and 31")
        if input_mm < 1 or input_mm > 12:
            raise ValueError(f"Invalid value {input_mm} for input_mm, it should be between 1 and 12")
        if input_yy < 2000 or input_yy > 2999:
            raise ValueError(f"Invalid value {input_yy} for input_yy, it should be between 2000 and 2999")

        self.dd = input_dd
        self.mm = input_mm
        self.yy = input_yy

    def year_month_diff(self, other_date):
        # Calculate year and month difference
        if self.yy > other_date.yy or (self.yy == other_date.yy and self.mm > other_date.mm):
            year_diff = self.yy - other_date.yy
            month_diff = self.mm - other_date.mm
            if month_diff < 0:
                year_diff -= 1
                month_diff += 12
        else:
            year_diff = other_date.yy - self.yy
            month_diff = other_date.mm - self.mm
            if month_diff < 0:
                year_diff -= 1
                month_diff += 12

        return year_diff, month_diff


# Example usage:
date1 = Date(10, 7, 2023)
date2 = Date(5, 3, 2020)

print("Date 1:", date1.get_date())
print("Date 2:", date2.get_date())

year_diff, month_diff = date1.year_month_diff(date2)
print(f"Year difference: {year_diff}")
print(f"Month difference: {month_diff}")
