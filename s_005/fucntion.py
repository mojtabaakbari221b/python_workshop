# def my_func():
#     a = 3 + 5
#     # return a

# print(my_func())

# def sum(a, b=6):
#     return a+b

# # print(sum(1))
# print(sum(b=1,a=9))

# def check_password(password):
#     if len(password) < 6 :
#         return False
    
#     if password == "seraj" or password == "code" :
#         return False
    
#     if "@" not in password :
#         return False
    
#     return True
    
#     # if password == "seraj" or password == "code" :
#     #     return False

# password = input("please insert your password: ")
# print(check_password(password=password))

# password2 = input("please insert your password2: ")
# print(check_password(password=password2))


# def my_sum(*args): # args is a tuple
#     return sum(args)

# print(my_sum(1,2,3,4,5,5,6,7,8,9))

# def a(a, b, c):
#     pass

# print(a(1,b=2,c=3))

# def my_sum(*args):
#     print(args)

# def my_sum(**kwargs):
#     print(kwargs)

# print(my_sum(a=1,b=2, c=4, d=6))

# def check_registration_rules(**kwargs):
#     valid_usernames = []

#     for key, value in kwargs.items():
#         print(key + " : " + value)
#         if key == "quera" :
#             continue

#         if len(value) < 4 :
#             continue

#         if value.isnumeric() : # int
#             continue

#         valid_usernames.append(key)
    
#     return valid_usernames


# print(check_registration_rules(username='1234', sadegh='He3@lsa', quera='kLS45@l$'))



