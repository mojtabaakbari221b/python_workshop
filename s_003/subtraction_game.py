number = input() 
my_list = list(number)
# 17 --> '17' -- convert to list --> [ '7' , '1' ] --> convert to integer ...

dahgan = int(my_list[0])
yekan = int(my_list[1])

max_number = max([ dahgan, yekan ])
min_number = min([ dahgan, yekan ])

print( max_number - min_number )

