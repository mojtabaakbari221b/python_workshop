try :
    a = int(input("please insert your sorat : "))
    b = int(input("please insert your makhraj : "))

    f = open("s_013/a.txt", "r")
    print(f.readlines())

    print(a / b)
except ZeroDivisionError :
    print("zero division error was accord.")
except FileNotFoundError :
    print("your file not founded.")
except ValueError as err :
    print(err)
    print("please insert valid numbers.")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished") 

print("the program ended :))")