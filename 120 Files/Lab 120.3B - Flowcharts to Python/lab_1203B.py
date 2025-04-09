alpha_part = [1,2,3,4,5,6,7,8,9,10]

item = int(input("Item number between 1 and 10: "))
while item < 1 or item > 10:
    print("Invalid number entered. Code failed")
    item = int(input("Item number between 1 and 10: "))


lower_bound = 0
upper_bound = len(alpha_part) - 1

found = False

while not found and lower_bound <= upper_bound:
    midpoint = (lower_bound + upper_bound) // 2
    if alpha_part[midpoint] == item:
        found = True
    else:
        if alpha_part[midpoint] < item:
            lower_bound = midpoint + 1
            pass
        else:
            upper_bound = midpoint - 1
            pass
else:
    if found:
        print("Item found at ", midpoint, "midpoint")
    else:
        print("Item not found")