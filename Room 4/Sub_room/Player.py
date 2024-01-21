import pygame
import subprocess
from random import shuffle

passwords = {1: 'hyefxt', 2: 'rwvnxz', 3: 'ctwldx', 4: 'lbimco', 5: 'mactuy', 6: 'fydaea'}
order = [1, 2, 3, 4, 5, 6]
shuffle(order)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_paths):
        super().__init__()
        self.img = [pygame.image.load(path) for path in image_paths]
        self.images = [pygame.transform.scale(img,(30,30)) for img in self.img]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def move(self, keys, border, treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, portal):
        new_position = self.rect.copy()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            new_position.y -= self.speed
            self.index = 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            new_position.y += self.speed
            self.index = 0
        if keys[pygame.K_a] or keys[pygame.K_RIGHT]:
            new_position.x += self.speed
            self.index = 3
        if keys[pygame.K_d] or keys[pygame.K_LEFT]:
            new_position.x -= self.speed
            self.index = 2

        self.image = self.images[self.index]

        # Check for collisions 
        if not any(new_position.colliderect(obstacle) for obstacle in border):
            self.rect.topleft = new_position.topleft
        
        if any(new_position.colliderect(obstacle) for obstacle in treasure1):
            message = str(order[0]) + ": " + passwords[order[0]]

        if any(new_position.colliderect(obstacle) for obstacle in treasure2):
            message = str(order[1]) + ": " + passwords[order[1]]

        if any(new_position.colliderect(obstacle) for obstacle in treasure3):
            message = str(order[2]) + ": " + passwords[order[2]]

        if any(new_position.colliderect(obstacle) for obstacle in treasure4):
            message = str(order[3]) + ": " +  passwords[order[3]]

        if any(new_position.colliderect(obstacle) for obstacle in treasure5):
            message = str(order[4]) + ": " + passwords[order[4]]

        if any(new_position.colliderect(obstacle) for obstacle in treasure6):
            message = str(order[5]) + ": " + passwords[order[5]]

        if any(new_position.colliderect(obstacle) for obstacle in portal):
            pygame.quit()
            subprocess.run(['python', 'room4.py'])