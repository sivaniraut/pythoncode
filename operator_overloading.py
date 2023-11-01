class Result:
    def __init__(self,subject1,subject2):
        self.subject1 = subject1
        self.subject2 = subject2


    def __add__(self, other):
        subject1 = self.subject1 + other.subject1
        subject2 = self.subject2 + other.subject2
        mark = Result(subject1,subject2)
        return mark

    def __gt__(self, other):
        result1 = self.subject1 + self.subject2
        result2 = self.subject1 + self.subject2
        if result1 > result2:
            return True
        else:
            return False

student1 = Result(50,40)
student2 = Result(70,55)

if student1 > student2:
    print("student 1 have highest mark")

else:
    print("student 2 have highest mark")


