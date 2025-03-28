import os

import pygame.sprite

BASE_PATH = './asset/Sprites/Rat/'


class Rat(pygame.sprite.Sprite):

    def __init__(self, position_y):
        super().__init__()
        self.sprites = []
        images = os.listdir(BASE_PATH)
        for img in images:
            self.sprites.append(pygame.image.load(BASE_PATH + img))

        self.position_y = position_y

        self.state = 0
        self.image = self.sprites[self.state]
        self.image = pygame.transform.flip(self.image, True, False).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = 850, self.position_y
        self.velocity = -1

    def update(self):
        self.state += 0.5
        if self.state >= len(self.sprites):
            self.state = 0
        self.image = self.sprites[int(self.state)]
        self.rect.x += self.velocity * 4

        self.image = pygame.transform.flip(self.image, True, False).convert_alpha()
