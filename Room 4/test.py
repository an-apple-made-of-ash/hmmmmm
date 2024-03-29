import os
import pygame
from pygame.locals import *
import pytmx
from pytmx import load_pygame


#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, image_paths, initial_position):
        super(Player,self).__init__()
        self.images = [pygame.image.load(path) for path in image_paths]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position

    def update(self): 
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            self.index=2
            self.rect.x -= 5
        if keys[K_RIGHT] or keys[K_d]:
            self.index=3
            self.rect.x += 5
        if keys[K_UP] or keys[K_w]:
            self.index=1
            self.rect.y -= 5
        if keys[K_DOWN] or keys[K_s]:
            self.index=0
            self.rect.y += 5

        self.image = self.images[self.index]
pygame.init() 

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Room 4")

#For Sprites 
assets_path = os.path.join(os.path.dirname(__file__), "..", "Assets")
paths = ["Delivery-Front.png","Delivery-Back.png","Delivery-Left.png","Delivery-Right.png"]
sprites = []
for path in paths: 
    sprite_path = os.path.join(assets_path, path)
    sprites.append(sprite_path)

player = Player(sprites,(100,100))

#Create sprite group and add player to it 
all_sprites = pygame.sprite.Group() 
all_sprites.add(player)

clock = pygame.time.Clock()

running = True 
while running: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
    
    all_sprites.update()

    screen.fill((0,0,0))

    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()