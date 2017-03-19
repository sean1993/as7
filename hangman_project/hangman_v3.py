import random

#List of words to choose from. 
list_of_words = ['cheese', 'glass', 'milk', 'cow']
letters_guessed = []
show_user = []

#number of times they can guess incorrectly
incorrect_guesses = 10

word = random.choice(list_of_words)
word = str(word)
#print(word)

for i in word:
    show_user.append('_')
print(' '.join(show_user))

while incorrect_guesses > 0:
    letter = raw_input("Enter a guess: ")
    if letter in word and letter not in letters_guessed:
        letters_guessed.append(letter)
        print(self.show_user_updated(letter, word, show_user))
        print(','.join(letters_guessed))
    elif letter not in word and letter not in letters_guessed:
        letters_guessed.append(letter)
        print(' '.join(show_user))
        print(','.join(letters_guessed))
    else:
        print("Not a valid guess")        
        
def show_user_updated(self, letter, word, show_user):
    i = 0
    while i < len(word):
        if letter == word[i]:
            show_user[i] = letter
            i+=1
        else:
            i+=1
    return ' '.join(show_user)
