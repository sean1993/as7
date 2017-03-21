import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
myfont = pygame.font.SysFont("monospace", 15)

while not done:
    label = myfont.render("Some Text!", 1, (255,255,0))
    screen.blit(label, (100, 100))
