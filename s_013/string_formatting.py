import statistics

points = [ 20, 12, 13]
student_name = "zahra"
my_site = "digikala.com"

def get_mean():
    return statistics.mean(points)

# print("point of " + student_name + " is " + str(point)) # point of zahra is 20

# old style
# my_str = "Hello %s, welcome to %s!" % (student_name, my_site)
# my_str = "Hello %(name)s, welcome to %(site)s!" % { "name" : student_name, "site" : my_site}

# print(my_str)

# new style
# my_str = "Hello {name}, welcome to {site}!".format(name=student_name, site=my_site)
# print(my_str)

# f-Strings
my_str = f"Hello {student_name}, welcome to {my_site}!, your mean is {get_mean()}"
print(my_str)

# template string
from string import Template
# my_str = Template("Hello $name, welcome to $site!")
# print(my_str.substitute(name=student_name, site=my_site))

name = input("insert your name : ")

my_str = Template("$name welcome to my site.")
print(my_str.substitute(name=name, site=my_site))
