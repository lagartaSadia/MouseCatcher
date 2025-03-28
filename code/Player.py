import os

import pygame

BASE_PATH = './asset/Sprites/Cat/'

class Player(pygame.sprite.Sprite):

    def __init__(self, dog_sprite, rat_sprite):
        super().__init__()
        self.sprites = []
        images = os.listdir(BASE_PATH)
        for img in images:
            self.sprites.append(pygame.image.load(BASE_PATH + img))

        self.lifes = 7
        self.rats_eaten = 0
        self.state = 0
        self.image = self.sprites[self.state]
        self.image = pygame.transform.scale(self.image, (38 * 1.2, 25 * 1.2)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = 50,200
        self.dog_sprite = dog_sprite
        self.rat_sprite = rat_sprite

    def update(self):
        self.state += 0.5
        if self.state >= len(self.sprites):
            self.state = 0
        self.image = self.sprites[int(self.state)]

        self.image = pygame.transform.scale(self.image, (38 * 1.2, 25 * 1.2)).convert_alpha()




    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 140:
            self.rect.centery -= 5
        elif pressed_key[pygame.K_DOWN] and  self.rect.top < 370:
            self.rect.centery += 5
        elif pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 5
        elif pressed_key[pygame.K_RIGHT] and self.rect.left < 760:
            self.rect.centerx += 5

    def check_if_collision(self):
        if pygame.sprite.spritecollide(self, self.dog_sprite, True, pygame.sprite.collide_mask):
            print("Dog Touched")
            self.lifes -= 1
            if self.lifes <= 0:
                print("Game Over")
        if pygame.sprite.spritecollide(self, self.rat_sprite, True, pygame.sprite.collide_mask):
            self.rats_eaten += 1
            print(f'You have eaten {self.rats_eaten} rats')