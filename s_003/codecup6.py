index = int(input()) # 17

index_char = (index % 8) - 1 # 1 == c

solution = {
    "0" : "c",
    "1" : "o",
    "2" : "d",
    "3" : "e",
    "4" : "c",
    "5" : "u",
    "6" : "p",
    "-1" : "6",
}

print(solution[str(index_char)])
