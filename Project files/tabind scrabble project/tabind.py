from collections import Counter

# we need this to count how many times each letter appears
# just like Counter("band") gives {'b':1, 'a':1, 'n':1, 'd':1}

def check(word, letters):
    # this is for checking if we can spell this word using only the letters we have
    # if the word needs 2 b but we only have 1, return False
    for char, count in Counter(word).items():
        if Counter(letters)[char] < count:
            return False
    return True

letters = "tabind"
results = []

with open("dictionary.txt", "r") as f:
    for line in f:
        word = line.strip().lower()
        if len(word) >= 2 and check(word, letters):
            results.append(word)

results.sort()

for word in results:
    print(word)