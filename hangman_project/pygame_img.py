import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hangman!")
hangman = pygame.image.load('hangman_test.png')
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(hangman, (50, 50))
    pygame.display.update()
