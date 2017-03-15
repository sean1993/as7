import random
words = ['cheese', 'egg', 'milk']
check = []
show = []
count = 0

word = random.choice(words)
word = str(word)

for i in word:
    check.append(i)
    show.append('_')
print(' '.join(show))
