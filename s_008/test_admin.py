import unittest
from q_t import login, Book, User


class TestAdmin(unittest.TestCase):
    def test_login(self):
        output = login(username="hasan", password="ali")

        self.assertEqual(output, False)

    def test_login_2(self):
        output = login(username="hasan", password="admin")

        self.assertEqual(output, True)



class TestUser(unittest.TestCase):
    def test_user_book_length_after_add(self):
        user = User(name="farzaneh", student_number=986532147)

        book1 = Book(name="clean code")
        book2 = Book(name="design pattern")

        self.assertEqual(len(user.books), 0)

        user.add_book(book1)
        user.add_book(book2)

        self.assertEqual(len(user.books), 2)

