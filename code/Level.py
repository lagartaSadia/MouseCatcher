import random

import pygame

from code.Const import EVENT_ENEMY, WHITE, WIN_WIDTH
from code.Dog import Dog
from code.Gameover import Gameover
from code.Menu import Menu
from code.Player import Player
from code.Rat import Rat


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.clock = pygame.time.Clock()
        self.color = (211, 211, 211)
        self.enemies_positions = [150, 200, 250, 300, 350]
        self.food_positions = [150, 200, 250, 300, 350]
        pygame.time.set_timer(EVENT_ENEMY, 1200)

    def run(self):
        forest = pygame.image.load('./asset/Background/forest.png')

        bridge = pygame.image.load('./asset/Background/bridge.png')

        grass = pygame.image.load('./asset/Background/grass.png')

        dog_sprites = pygame.sprite.Group()
        rat_sprites = pygame.sprite.Group()

        player = Player(dog_sprites, rat_sprites)

        level_text = Menu(self.window)

        cat_sprites = pygame.sprite.Group()
        cat_sprites.add(player)

        while True:
            self.clock.tick(30)

            self.window.blit(forest, forest.get_rect())

            self.window.blit(bridge, (0, 133))
            self.window.blit(grass, (0, 300))

            level_text.menu_text(30, f'{player.lifes} lifes', (0, 0, 0), ((WIN_WIDTH / 2), 30))
            level_text.menu_text(30, f'{player.rats_eaten} rats eaten', (0, 0, 0), ((WIN_WIDTH / 2), 80))

            cat_sprites.draw(self.window)
            cat_sprites.update()

            rat_sprites.draw((self.window))
            rat_sprites.update()

            dog_sprites.draw((self.window))
            dog_sprites.update()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = Menu(self.window)
                        menu.run()
                if event.type == EVENT_ENEMY:
                    if random.randint(1, 5) == 5:
                        rat = Rat(random.choice(self.food_positions))
                        rat_sprites.add(rat)
                    else:
                        dog = Dog(random.choice(self.enemies_positions))
                        dog_sprites.add(dog)

            player.move()
            player.check_if_collision()

            if player.lifes <= 0:
                Gameover(self.window).run(player.rats_eaten)