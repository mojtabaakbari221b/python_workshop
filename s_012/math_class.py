def add_point(point):
    with open("s_012/math_class_points.txt", "a") as f :
        f.write(str(point)+",")

def get_mean():
    with open("s_012/math_class_points.txt", "r") as f :
        line = f.readline()

        list_of_points = line.split(",")

        sum_of_points = 0
        count_of_points = 0

        for point in list_of_points :
            if point == "" :
                continue

            sum_of_points += int(point)
            count_of_points += 1
        
        print(sum_of_points / count_of_points)

while True :
    o = input("insert your action, if wana add point insert 1, get mean insert 2, break insert 0 :: ")
    if o == "0" :
        break

    if o == "1" :
        point = input("insert your new point : ")
        add_point(point)

    if o == "2" :
        get_mean()