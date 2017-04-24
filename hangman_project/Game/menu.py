import pygame, random, os
from pygame.locals import *
'''level = 1'''
secret_word = []
guessed = []
shown_letters = []
incorrect_guesses = 0
level = 1

def start_menu(screen):
    font = pygame.font.SysFont("Arial", 35)
    background = pygame.Surface((50, 50))
    background.fill((255, 255, 255))
    header = font.render("HANGMAN!", True, (0, 0, 0))
    begin = font.render("Begin", True, (0, 0, 0))
    difficulty = font.render("Difficulty", True, (0, 0, 0))
    quit = font.render("Quit", True, (0, 0, 0))
    while 1:
        screen.fill((255, 255, 255))
        screen.blit(header, (165, 100))
        screen.blit(begin, (165, 200))
        screen.blit(difficulty, (165, 260))
        screen.blit(quit, (165, 320))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 200 and e.pos[1] <= 235:
                    hangman(screen)
                elif e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 260 and e.pos[1] <= 295:
                    choose_difficulty(screen)
                elif e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 320 and e.pos[1] <= 355:
                    exit()
        pygame.display.update()

def choose_difficulty(screen):
    global level
    font = pygame.font.SysFont("Arial", 35)
    background = pygame.Surface((50, 50))
    background.fill((255, 255, 255))
    header = font.render("HANGMAN!", True, (0, 0, 0))
    easy = font.render("Easy", True, (0, 0, 0))
    normal = font.render("Normal", True, (0, 0, 0))
    hard = font.render("Hard", True, (0, 0, 0))
    while 1:
        screen.fill((255, 255, 255))
        screen.blit(header, (165, 100))
        screen.blit(easy, (165, 200))
        screen.blit(normal, (165, 260))
        screen.blit(hard, (165, 320))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 200 and e.pos[1] <= 235:
                    level == 1
                    return level
                    start_menu(screen)
                elif e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 260 and e.pos[1] <= 295:
                    level == 2
                    return level
                    start_menu(screen)
                elif e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 320 and e.pos[1] <= 355:
                    level == 3
                    return level
                    start_menu(screen)
        pygame.display.update()

def choose_word():
    words = []
    with open("data/easy.txt", "r") as f:
        for line in f:
            line = filter(None, line.strip().split(","))
            for word in line:
                words.append(word)
    word = random.choice(words)
    for i in word:
        secret_word.append(i)
        shown_letters.append('_')
    return secret_word, shown_letters

def update(letter):
    global incorrect_guesses
    if letter not in secret_word and letter not in guessed:
        incorrect_guesses += 1
        guessed.append(letter)
    elif letter in secret_word and letter not in guessed:
        for i in range(0, len(secret_word)):
            if secret_word[i] == letter:
                shown_letters[i] = letter
                guessed.append(letter)
        return incorrect_guesses

def hangman(screen):
    choose_word()
    font = pygame.font.SysFont("Arial", 25)
    while incorrect_guesses < 6 and shown_letters != secret_word:
        if incorrect_guesses == 6 or shown_letters == secret_word:
            endgame(screen)
        screen.fill((255, 255, 255))
        screen.blit(font.render("Word: " + ' '.join(shown_letters), True, (0, 0, 0)), (50, 500))
        screen.blit(font.render("Already Guessed: " + ','.join(sorted(guessed)), True, (0, 0, 0)), (50, 550))
        screen.blit(font.render(str(incorrect_guesses) + "/6", True, (0, 0, 0)), (50, 600))
        screen.blit(pygame.image.load(os.path.join("data/hangman_0.png")), (0, 0))
        if incorrect_guesses > 0:
            screen.blit(pygame.image.load(os.path.join("data/hangman_" + str(incorrect_guesses) + ".png")), (0, 0))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_a:
                    update("a")
                elif e.key == K_b:
                    update("b")
                elif e.key == K_c:
                    update("c")
                elif e.key == K_d:
                    update("d")
                elif e.key == K_e:
                    update("e")
                elif e.key == K_f:
                    update("f")
                elif e.key == K_g:
                    update("g")
                elif e.key == K_h:
                    update("h")
                elif e.key == K_i:
                    update("i")
                elif e.key == K_j:
                    update("j")
                elif e.key == K_k:
                    update("k")
                elif e.key == K_l:
                    update("l")
                elif e.key == K_m:
                    update("m")
                elif e.key == K_n:
                    update("n")
                elif e.key == K_o:
                    update("o")
                elif e.key == K_p:
                    update("p")
                elif e.key == K_q:
                    update("q")
                elif e.key == K_r:
                    update("r")
                elif e.key == K_s:
                    update("s")
                elif e.key == K_t:
                    update("t")
                elif e.key == K_u:
                    update("u")
                elif e.key == K_v:
                    update("v")
                elif e.key == K_w:
                    update("w")
                elif e.key == K_x:
                    update("x")
                elif e.key == K_y:
                    update("y")
                elif e.key == K_z:
                    update("z")
                else:
                    screen.blit(font.render("Invalid button", True, (0, 0, 0)), (50, 650))
            pygame.display.update()

def endgame(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("Arial", 35)
    winner = font.render("YOU WIN!!!", True, (0, 0, 0))
    loser = font.render("YOU LOSE!!!", True, (0, 0, 0))
    if incorrect_guesses == 6:
        screen.blit(loser, (165, 200))
        screen.blit(font.render("Back to main menu", True, (0, 0, 0)), (165, 250))
    else:
        screen.blit(winner, (165, 200))
        screen.blit(font.render("Back to main menu", True, (0, 0, 0)), (165, 250))