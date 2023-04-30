from math import factorial
from math import pow


def calculate_exponential_func(x, n):
    my_sum = 0
    for i in range(0, n+1):
        my_sum += pow(x, i) / factorial(i)

    return my_sum

# print(calculate_exponential_func(n=10, x=5))