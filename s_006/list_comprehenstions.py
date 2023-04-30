# my_list = []

# for item in range(4):
#     my_list.append(item)

# my_list = [ i * 2 for i in range(4) ]

# [ expression for item in list ]
# 
# for item in list :
#   expression 

# print(my_list)

# my_list = []

# for i in range(10):
#     if i % 2 == 0 :
#         my_list.append(i**2)

# n = int(input())

# my_list = [ item**2 for item in range(n) if item % 2 == 0 ]

# print(my_list)

def my_func():
    print("Hello World!")

for i in range(5):
    # print(i**2)
    my_func()

[ my_func() for _ in range(5) ]

