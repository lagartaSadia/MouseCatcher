import random

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, EVENT_ENEMY
from code.Dog import Dog
from code.Menu import Menu
from code.Player import Player


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.clock = pygame.time.Clock()
        self.color = (211,211,211)
        self.enemies_positions = [150, 200, 250, 300, 350]
        pygame.time.set_timer(EVENT_ENEMY, 800)

    def run(self):
        forest = pygame.image.load('./asset/Background/forest.png')

        bridge = pygame.image.load('./asset/Background/bridge.png')

        grass = pygame.image.load('./asset/Background/grass.png')

        dog_sprites = pygame.sprite.Group()
        player = Player(dog_sprites)
        cat_sprites = pygame.sprite.Group()
        cat_sprites.add(player)

        while True:
            self.clock.tick(30)

            self.window.blit(forest, forest.get_rect())

            self.window.blit(bridge, (0, 133))
            self.window.blit(grass, (0, 300))

            cat_sprites.draw(self.window)
            cat_sprites.update()

            dog_sprites.draw((self.window))
            dog_sprites.update()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = Menu(self.window)
                        menu.run()
                if event.type == EVENT_ENEMY:
                    dog = Dog(random.choice(self.enemies_positions))
                    dog_sprites.add(dog)


            player.move()
            player.check_if_collision()
