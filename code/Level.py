import pygame

from code.Menu import Menu


class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name

    def run(self):
        surf = pygame.image.load('./asset/Background/2/forestbridge.png')
        rect = surf.get_rect()
        player = pygame.image.load('./asset/Sprites/Cat walk1.png')

        while True:
            self.window.blit(surf, rect)
            self.window.blit(player, (100, 200))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = Menu(self.window)
                        menu.run()