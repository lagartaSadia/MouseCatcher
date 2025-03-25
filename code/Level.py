import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
from code.Player import Player


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.clock = pygame.time.Clock()

    def run(self):
        forest = pygame.image.load('./asset/Background/forest.png')

        bridge = pygame.image.load('./asset/Background/bridge.png')

        grass = pygame.image.load('./asset/Background/grass.png')

        player = Player()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

        while True:
            self.clock.tick(30)

            self.window.blit(forest, forest.get_rect())


            self.window.blit(bridge, (0, 133))
            self.window.blit(grass, (0, 300))

            all_sprites.draw(self.window)
            all_sprites.update()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = Menu(self.window)
                        menu.run()
                    if event.key == pygame.K_w:
                        player.update('up')
                    if event.key == pygame.K_s:
                        player.update('down')