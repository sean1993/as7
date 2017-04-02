import random, pygame, sys
pygame.init()
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Hangman!")
done = False
words = ['cheese', 'egg', 'milk']

while not done:
    word = random.choice(words)
    word = str(word)
    guessed = ''
    incorrect_guesses = 6
    myfont = pygame.font.SysFont("Arial", 30)

    while incorrect_guesses > 0:    
        failed = 0
        for char in word:
            if char in guessed:
                label = myfont.render(char, 1, (255,255,255))
            else:
                label = myfont.render("_", 1, (255,255,255))
                failed += 1
        if failed == 0:
            print("\nCorrect!")
            break

        print ''
        letter = raw_input("\nGuess a letter: ")
        if letter in guessed:
            while letter in guessed:
                letter = raw_input("\nAlready guessed. Guess again: ")
                if letter not in guessed:
                    guessed += letter
                    break
        else:
            if letter.islower():
                guessed += letter
            else:
                letter = raw_input("\nInvalid letter. Guess again: ")
            
                

        if letter not in word:
            incorrect_guesses -= 1
            print("\nIncorrect!")
            if incorrect_guesses == 0:
                print("\nGAME OVER!!")
                break
        print("Letters already guessed: " + '-'.join(sorted(guessed)))
