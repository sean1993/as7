import random
words = ['cheese', 'egg', 'milk']

name = raw_input("Please enter your name: ")

print("Hello " + name + " lets play a game of hangman!")
print("\n")

print("Lets Play!")
print ''
word = random.choice(words)
word = str(word)
guessed = ''
incorrect_guesses = 6

while incorrect_guesses > 0:
    
    failed = 0
    for char in word:
        if char in guessed:
            print char,
        else:
            print "_",
            failed += 1
    if failed == 0:
        print("\nCorrect!")
        break

    print ''
    letter = raw_input("\nGuess a letter: ")
    if letter.islower():
        guessed += letter
    else:
        letter = raw_input("\nInvalid letter. Guess again: ")

    if letter not in word:
        incorrect_guesses -= 1
        print("\nIncorrect!")
        if incorrect_guesses == 0:
            print("\nYou failed!")
