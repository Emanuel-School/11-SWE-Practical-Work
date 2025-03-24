#inputs
from random import randint

#Wordlist
WD_Orig = open("Wordlist.txt", "r")
WD = WD_Orig.read().splitlines()
#Set beginning and end word

S_Word = WD[randint(0, len(WD) - 1)]
E_Word = WD[randint(0, len(WD) - 1)]

while True:
    print("Testing: " + S_Word)
    print("Testing: " + E_Word)

    if S_Word == E_Word:
        E_Word = WD[randint(0, len(WD) - 1)]
    else:
        break

print(f"Starting word is: {S_Word}")
print(f"Ending word is: {E_Word}")