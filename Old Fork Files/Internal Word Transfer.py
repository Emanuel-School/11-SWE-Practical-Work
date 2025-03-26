from random import randint

WordsList = ["Brick", "Sharp", "Words", "Cloud", "flash"]

GameList = []

word1 = WordsList.pop(randint(0, len(WordsList) - 1))
word2 = WordsList.pop(randint(0, len(WordsList) - 1))

GameList.append(word1)
GameList.append(word2)

print(GameList)