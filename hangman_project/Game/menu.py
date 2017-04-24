import pygame, random, os
from pygame.locals import *
'''level = 1'''
secret_word = []
incorrect_guesses = 0
guessed = []
shown_letters = []

def start_menu(screen):
    font = pygame.font.SysFont("Arial", 35)
    background = pygame.Surface((50, 50))
    background.fill((255, 255, 255))
    header = font.render("HANGMAN!", True, (0, 0, 0))
    begin = font.render("Begin", True, (0, 0, 0))
    #difficulty = font.render("Difficulty", True, (0, 0, 0))
    quit = font.render("Quit", True, (0, 0, 0))
    while 1:
        screen.fill((255, 255, 255))
        screen.blit(header, (165, 100))
        screen.blit(begin, (165, 200))
        #screen.blit(difficulty, (165, 260))
        screen.blit(quit, (165, 320))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 200 and e.pos[1] <= 235:
                    hangman(screen)
                #elif e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 260 and e.pos[1] <= 295:
                    #choose_difficulty(screen)
                elif e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 320 and e.pos[1] <= 355:
                    exit()
        pygame.display.update()

'''
def choose_difficulty(screen):
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
                    level = 1
                    return level
                    start_menu(screen)
                elif e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 260 and e.pos[1] <= 295:
                    level = 2
                    return level
                    start_menu(screen)
                elif e.pos[0] >= 165 and e.pos[0] <= 265 and e.pos[1] >= 320 and e.pos[1] <= 355:
                    level = 3
                    return level
                    start_menu(screen)
        pygame.display.update()
'''

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
    shown_letters.append("_" * len(word))
    return secret_word

def update(letter):
    if letter in secret_word and letter not in guessed:
        correct = False
        for i in range(1, len(secret_word)-1):
            if secret_word[i] == letter:
                shown_letters[i] = letter
                guessed.append(letter)
                correct = True
        if not correct:
            incorrect_guesses += 1
            guessed.append(letter)

def hangman(screen):
    font = pygame.font.SysFont("Arial", 25)
    winner = font.render("YOU WIN!!!", True, (0, 0, 0))
    loser = font.render("YOU LOSE!!!", True, (0, 0, 0))
    while incorrect_guesses < 6:
        screen.fill((255, 255, 255))
        screen.blit(font.render("Guess " + str(incorrect_guesses + 1) + ": " , True, (0, 0, 0)), (50, 500))
        screen.blit(font.render("Already Guessed: ", True, (0, 0, 0)), (50, 550))
        screen.blit(pygame.image.load(os.path.join("data/hangman_0.png")), (0, 0))
        if incorrect_guesses > 0:
            screen.blit(pygame.image.load(os.path.join("data/hangman_" + str(incorrect_guesses) + ".png")), (0, 0))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_a:
                    secret_word.update("a")
                elif e.key == K_b:
                    secret_word.update("b")
                elif e.key == K_c:
                    secret_word.update("c")
                elif e.key == K_d:
                    secret_word.update("d")
                elif e.key == K_e:
                    secret_word.update("e")
                elif e.key == K_f:
                    secret_word.update("f")
                elif e.key == K_g:
                    secret_word.update("g")
                elif e.key == K_h:
                    secret_word.update("h")
                elif e.key == K_i:
                    secret_word.update("i")
                elif e.key == K_j:
                    secret_word.update("j")
                elif e.key == K_k:
                    secret_word.update("k")
                elif e.key == K_l:
                    secret_word.update("l")
                elif e.key == K_m:
                    secret_word.update("m")
                elif e.key == K_n:
                    secret_word.update("n")
                elif e.key == K_o:
                    secret_word.update("o")
                elif e.key == K_p:
                    secret_word.update("p")
                elif e.key == K_q:
                    secret_word.update("q")
                elif e.key == K_r:
                    secret_word.update("r")
                elif e.key == K_s:
                    secret_word.update("s")
                elif e.key == K_t:
                    secret_word.update("t")
                elif e.key == K_u:
                    secret_word.update("u")
                elif e.key == K_v:
                    secret_word.update("v")
                elif e.key == K_w:
                    secret_word.update("w")
                elif e.key == K_x:
                    secret_word.update("x")
                elif e.key == K_y:
                    secret_word.update("y")
                elif e.key == K_z:
                    secret_word.update("z")
                else:
                    screen.blit(font.render("Invalid button", True, (0, 0, 0)), (50, 600))
            pygame.display.update()
    while 1:
        screen.fill((255, 255, 255))
        if incorrect_guesses == 6:
            screen.blit(loser, (165, 200))
        else:
            screen.blit(winner, (165, 200))
        screen.blit(font.render("Back to main menu", True, (0, 0, 0)), ())