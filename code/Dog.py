import os

import pygame

BASE_PATH = './asset/Sprites/Dog/'

class Dog(pygame.sprite.Sprite):
    def __init__(self, position_y):
        super().__init__()
        self.sprites = []
        images = os.listdir(BASE_PATH)
        for img in images:
            self.sprites.append(pygame.image.load(BASE_PATH + img))

        self.position_y = position_y

        self.state = 0
        self.image = self.sprites[self.state]
        self.image = pygame.transform.flip(pygame.transform.scale(self.image, (38 * 2, 25 * 2)), True, False).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = 850, self.position_y
        self.velocity = -1

    def update(self):
        self.state += 0.5
        if self.state >= len(self.sprites):
            self.state = 0
        self.image = self.sprites[int(self.state)]
        self.rect.x += self.velocity * 3

        self.image = pygame.transform.flip(pygame.transform.scale(self.image, (38 * 2, 25 * 2)), True, False).convert_alpha()
