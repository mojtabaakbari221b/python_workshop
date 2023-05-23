# f = open("s_012/points.txt", "r")
# # f = open("/home/mojtaba/w/workshops/python_workshop/s_012/points.txt", "r")
# # f = open("D:\\PYTHON\points.txt", "r")

# print(f.readline())
# print(f.readline())

# f.close()

with open("s_012/points.txt", "r") as f :
    points = f.readlines()

    sum_points = 0
    count_points = 0

    for point in points :
        a = int(point.strip())

        sum_points += a
        count_points += 1

    print(sum_points)
    print(count_points)

    print(sum_points / count_points)

    # f.write("20")


with open("s_012/new_point.txt", "w") as f2 :
    f2.write("20")

with open("s_012/new_point2.txt", "a") as f2 :
    f2.write("20")