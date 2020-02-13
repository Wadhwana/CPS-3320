def letterScore(letter):
    if letter in 'aeilnorstuv':
        return 1
    elif letter in 'dg':
        return 2
    elif letter in 'bcmp':
        return 3
    elif letter in 'fhwy':
        return 4
    elif letter in 'k':
        return 5
    elif letter in 'jx':
        return 8
    elif letter in 'qz':
        return 10
    else:
        return 0


def wordScore(word):
    total = 0
    for l in word:
        l = l.lower()
        score = letterScore(l)
        total = total + score
    return total


w = input("Enter the word: ")  # type: string
value = wordScore(w)
print("word score is: ", value)
