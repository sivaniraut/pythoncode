class student:
    school = "DAV school"
    standard = "10 B"

    def __init__(self,sub1,sub2,sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def total_mark(self,):
        return int(self.sub1 + self.sub2 + self.sub3)
    def average(self,):
        return int((self.sub1 + self.sub2 + self.sub3)/3)

    @classmethod
    def information(cls):
        return cls.school

student1 = student(50,70,65)
student2 = student(90,80,35)

total_mark1 = student1.total_mark()

avg_student1 = student1.average()
avg_student2 = student2.average()

print(f"Student 1 total mark:{total_mark1}")
print(f"Student 1 average mark:{avg_student1}")
print(student1.information())


print("=" * 80)
print(f"Student 2 average mark:{avg_student2}")
print(student1.information())

