n = int(input("please insert your n : "))
m = int(input("please insert your m : "))

counter = 0

for i in range(n*m):
    char = input("please insert your char : ")

    if char == "*" :
        counter += 1

print(counter)
