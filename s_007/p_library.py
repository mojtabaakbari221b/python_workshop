from p_library_book import Book
from p_library_manager import Manager
from getpass import getpass

books = []



while True :
    name = input("please insert yout name : ")
    password = password = getpass("please insert your password : ")

    if name == "admin" and password == "admin":
        print("correct admin ...")

        



    else :
        print("incorrect admin ...")


