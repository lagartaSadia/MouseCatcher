import os

import pygame

BASE_PATH = './asset/Sprites/Cat/'

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprites = []
        images = os.listdir(BASE_PATH)
        for img in images:
            print(img)
            self.sprites.append(pygame.image.load(BASE_PATH + img))

        self.state = 0
        self.image = self.sprites[self.state]
        self.image = pygame.transform.scale(self.image, (38 * 1.5, 25 * 1.5))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100,200

    def update(self):
        self.state += 0.05
        if self.state >= len(self.sprites):
            self.state = 0
        self.image = self.sprites[int(self.state)]
        self.rect.left += 1
        self.image = pygame.transform.scale(self.image, (38 * 1.5, 25 * 1.5))
