# Lab 120.3A - Pseudocode to Python

count = 0
num = 0

def process_number(x):
    if x % 3 == 0 and x % 5 == 0:
        print("Fizzbuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

while num >= 0:
    num = int(input("Enter a number: "))
    if num >= 0:
        count += 1
        process_number(num)
    else:
        print("Negative number entered. Ending output")

print("Numbers processed: " + str(count))