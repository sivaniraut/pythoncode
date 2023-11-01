
"""
Create class of human

Create class of student

Create class of employee


Studetn -> Human [-> Object]

Employee -> Student -> Human [-> Object]

"""


# Base class or parent class
class Human:
    def __init__(self, ):
        self.first_name = ""
        self.last_name = ""
        self.birth_date = ""

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_bod(self, bod):
        self.birth_date = bod

    def __str__(self):
        return (f"\nName: {self.get_name()}\n"
                f"BOD: {self.birth_date}")

    def test_01(self, ):
        print("I am in Human Class, Method test 01")

    def test_02(self, ):
        print("I am in Human Class, Method test 02")

        # (Base Class or Parent Class)


# Child class or Drvied class
# MRO => Student -> Human ->. ...-> object
class Student(Human):
    def __init__(self, ):
        self.institute_name = ""

    def set_institute_name(self, institute_name):
        self.institute_name = institute_name

    def get_institute_name(self, ):
        return self.institute_name

    def __str__(self):
        return (f"{Human.__str__(self)}"
                f"Institute Name: {self.get_institute_name()}")

    def test_01(self, ):
        print("I am in Student Class, Method test 01")

    def test_03(self, ):
        print("I am in Student Class, Method test 03")


class OriginalStudent:
    def __init__(self, ):
        self.first_name = ""
        self.last_name = ""
        self.birth_date = ""
        self.institute_name = ""

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_bod(self, bod):
        self.birth_date = bod

    def set_institute_name(self, institute_name):
        self.institute_name = institute_name

    def get_institute_name(self, ):
        return self.institute_name

    def __str__(self):
        return (f"\nName: {self.get_name()}\nBOD: {self.birth_date}\n"
                f"Institute Name: {self.get_institute_name()}")

    def test_01(self, ):
        print("I am in Student Class, Method test 01")

    def test_03(self, ):
        print("I am in Student Class, Method test 03")


class Employee(Student):
    def __init__(self, ):
        self.first_name = ""
        self.last_name = ""
        self.birth_date = ""
        # self.institute_name = ""
        self.company_name = ""
        self.basic_salary = 0

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_bod(self, bod):
        self.birth_date = bod

    def set_company_name(self, company_name: str) -> None:
        self.company_name = company_name

    def set_basic_salary(self, basic_salary: int) -> None:
        self.basic_salary = basic_salary

    def get_salary(self, ) -> float:
        return self.basic_salary + (self.basic_salary * 0.30)

    def __str__(self):
        return (f"\nName: {self.get_name()}\nBOD: {self.birth_date}\n"
                f"Company Name: {self.company_name}\n"
                f"Basic Salary: {self.get_salary()}")

    def test_01(self, ):
        print("I am in Employee Class, Method test 01")

    def test_02(self, ):
        print("I am in Employee Class, Method test 02")

    def test_04(self, ):
        print("I am in Employee Class, Method test 04")

    # human_obj = Human()


# human_obj.set_name("Vivek",  "Sable")
# human_obj.set_bod("29/10/1988")
# print("human_obj:", human_obj)
# human_obj.test_01()
# human_obj.test_02()
# print("="*80)
student_obj = Student()
student_obj.set_name("Sivani", "Raut")
student_obj.set_bod("09/09/1994")
student_obj.set_institute_name("BPUT, BBSR")
print("student_obj:", student_obj)
student_obj.test_01()
student_obj.test_02()
student_obj.test_03()  # Student.test_03(student_obj)

print("=" * 80)
exit(0)
emp_obj = Employee()
emp_obj.set_name("Sivani", "Raut")
emp_obj.set_bod("09/09/1994")
emp_obj.set_company_name("HCL")
emp_obj.set_basic_salary(10000)
print("emp_obj:", emp_obj)
emp_obj.test_01()
emp_obj.test_02()
emp_obj.test_04()
print("=" * 80)