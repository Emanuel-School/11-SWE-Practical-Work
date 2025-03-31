from math import sqrt

num = int(input("Enter a number: "))

if num < 2:
    print("Not prime")
else:
    prime = True

for i in range(2, int(sqrt(num))):
    if num % i == 0:
        prime = False
        break
    if prime == True:
        print("prime")
    else:
        print("not prime")

