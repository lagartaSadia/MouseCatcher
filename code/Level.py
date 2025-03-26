import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
from code.Player import Player


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.clock = pygame.time.Clock()
        self.color = (211,211,211)

    def run(self):
        forest = pygame.image.load('./asset/Background/forest.png')

        bridge = pygame.image.load('./asset/Background/bridge.png')

        grass = pygame.image.load('./asset/Background/grass.png')

        player = Player()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

        while True:
            self.clock.tick(30)

            top_wall = pygame.draw.rect(self.window, self.color, pygame.Rect(30, 45, 100, 80))
            bottom_wall = pygame.draw.rect(self.window, self.color, pygame.Rect(45, 400, 100, 20))

            self.window.blit(forest, forest.get_rect())

            self.window.blit(bridge, (0, 133))
            self.window.blit(grass, (0, 300))

            cat = all_sprites.draw(self.window)
            all_sprites.update()

            if top_wall.colliderect(player) or bottom_wall.colliderect(player):
                player.velocity = 0

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

    def crash(self, cat, enemy):

        pass