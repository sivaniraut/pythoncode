class Complex_num:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        output_complex = Complex_num(real,imaginary)

        return output_complex

a = Complex_num(3,5)
b = Complex_num(4,2)

final_output = a + b

print(f"Output: {final_output.real} + {final_output.imaginary}i")



class Complex_num:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        output_complex = Complex_num(real,imaginary)

        return output_complex

a = Complex_num(8,5)
b = Complex_num(4,3)

final_output = a - b

print(f"Output: {final_output.real} - {final_output.imaginary}i")