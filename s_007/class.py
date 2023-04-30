class Student():
    student_number = int()
    phone_numebr = str()
    name = str()

    def __init__(self, my_name, my_student_number, my_phone_number): # __init__
        self.name = my_name
        self.student_number = my_student_number
        self.phone_numebr = my_phone_number

    def take_a_course(self):
        pass

    def take_a_food(self):
        pass

student1 = Student(my_name="ali", my_student_number=9832531, my_phone_number="+989653214568")

student2 = Student(my_name="hosein", my_student_number=9856651, my_phone_number="+8985945231")


print("student1 name : " + str(student1.name))

print("student2 name : " + str(student2.name))

# def Student():
#     name = "ali"

# Student.name


# student1.name = int()


# print(type(Student.name))

# student1 = Student()
# student1.name = "ali hoseisi"
# student1.student_number = 983552345
# student1.phone_numebr = "09531651613"

# print(Student)

# print(student1.name)
# print(student1.student_number)


# name1 = "fatemh .."
# student1 = "8567423"

# name2 = "ali ..."
# student2 = "98123213"