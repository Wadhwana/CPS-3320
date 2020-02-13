import random
# Hangman game!
# Assume the answer is "hangman"
A = ['h','a','n','g','m','a','n']
L = ['_','_','_','_','_','_','_']

wordList = ['aishwik', 'wadhwani', 'python', 'programming', 'hangman', 'results']
print("You have to guess a random word from the list")

with open("input.txt") as input:
    wordList = input.read().split(" ")


word = random.choice(wordList)
A = list(word)

L = []
for i in A:
    L.append('_')


play = True
wrong = 0
while play == True:
    # Ask the user to guess a letter
    letter = input("Guess a letter: ") # type: String
    # Check to see if that letter is in the Answer
    i = 0
    if letter in A:
        for currentletter in A:
        # If the letter the user guessed is found in the answer,
        # set the underscore in the user's answer to that letter

            if letter == currentletter:
                L[i] = letter
            i = i + 1
        # Display what the player has thus far (L) with a space
        # separating each letter
        print(' '.join(str(n) for n in L))
    else:
        print("BAD GUESS")
        wrong = wrong + 1
        if wrong == 6:
            print("SORRY! YOU LOOSE!!!")
            play = False
    # Test to see if the word has been successfully completed,
    # and if so, end the loop
    if A == L:
        play = False
        print("GREAT JOB!")