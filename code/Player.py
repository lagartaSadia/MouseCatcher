import os

import pygame

BASE_PATH = './asset/Sprites/Cat/'

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprites = []
        images = os.listdir(BASE_PATH)
        for img in images:
            self.sprites.append(pygame.image.load(BASE_PATH + img))

        self.state = 0
        self.image = self.sprites[self.state]
        self.image = pygame.transform.scale(self.image, (38 * 2, 25 * 2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 50,200
        self.velocity = 0

    def update(self, direction = None):
        self.state += 0.5
        if self.state >= len(self.sprites):
            self.state = 0
        self.image = self.sprites[int(self.state)]
        self.rect.y += self.velocity * 5

        match direction:
            case 'up':
                self.velocity = -1
            case 'down':
                self.velocity = 1

        self.image = pygame.transform.scale(self.image, (38 * 2, 25 * 2))
