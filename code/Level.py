import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
from code.Player import Player


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name

    def run(self):
        surf = pygame.image.load('./asset/Background/forestbridge.png')
        rect = surf.get_rect()
        player = Player()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

        while True:
            self.window.blit(surf, rect)
            # self.window.blit(player, ((WIN_WIDTH / 2), (WIN_HEIGHT / 2)))
            all_sprites.draw(self.window, )
            all_sprites.update()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = Menu(self.window)
                        menu.run()