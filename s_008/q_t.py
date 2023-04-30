users = []


class User():
    books = []

    def __init__(self, name, student_number) -> None:
        self.name = name
        self.student_number = student_number

    def add_book(self, book):
        self.books.append(book)


class Book():
    def __init__(self, name) -> None:
        self.name = name


def login(username, password):
    if password == "admin" :
        return True
    
    return False

