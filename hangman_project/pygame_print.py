import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hangman!")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    myfont = pygame.font.SysFont("Arial", 40)
    label = myfont.render("Some Text!", 1, (255,255,255))
    screen.blit(label, (100, 100))
    pygame.display.update()
