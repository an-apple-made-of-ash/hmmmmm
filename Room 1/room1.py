import os
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
pic = pygame.image.load("Assets/concrete floor.png")
screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
pygame.display.flip()
while True:

    #generate concrete background floor
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.display.quit()
    elif event.type == VIDEORESIZE:
        screen = pygame.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
        pygame.display.flip()

    