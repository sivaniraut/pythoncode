class Book:

    def __init__(self,name, author, edition):
        self.name = name
        self.author = author
        self.edition = edition

    def __str__(self):
        return f"The Book Name {self.name}\n The Author {self.author}\n " \
               f"This is {self.edition}"


book = Book("Python Programmimg", "Reema", "Second Edition")
print(book)


