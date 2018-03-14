import pygame, sys
from pygame.locals import *


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("atlanta-city")

background = pygame.image.load("default.png").convert()
car = pygame.image.load("car.png").convert_alpha()

Px = 640
Py = 360
Cx = 0
Cy = 0
class Entity(pygame.sprite.Sprite):
    def __init__(self, velocity, image):
        pygame.sprite.Sprite.__init__(self)
        self.image.load(image)

while True: #main game loop
    for event in pygame.event.get(): #event catcher
        if event.type == QUIT:
            quit()
            sys.exit()

    Pvx = 0
    Pvy = 0
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[K_w]:
        Pvy -= 1
    if keys[K_s]:
        Pvy += 1
    if keys[K_d]:
        Pvx += 1
    if keys[K_a]:
        Pvx -= 1

    Cx -= Pvx
    Cy -= Pvy
    screen.blit(background, (Cx,Cy))
    screen.blit(car, (Px, Py))


    
    pygame.display.update()