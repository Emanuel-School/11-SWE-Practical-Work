from random import randint

GameList = []

with open("wordlist.txt", "r") as file:
    words = file.read().splitlines()

word1 = words.pop(randint(0, len(words) - 1))

word2 = words.pop(randint(0, len(words) - 1))

GameList.append(word1)
GameList.append(word2)

print(GameList)