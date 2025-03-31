from math import sqrt

num = int(input("Enter a number: "))
prime = True

if num < 2:
    print("Not prime")
    prime = False
for i in range(2, int(sqrt(num))+1):
    if num % i == 0:
        prime = False
        break

if prime == True:
    print("prime")
else:
    print("not prime")

