import pygame, sys
from pygame.locals import *
pygame.init()
display_surface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("atlanta-city")

while True: #main game loop
    for event in pygame.event.get(): #nasluchiwanie
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()