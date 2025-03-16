import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600,600))

    def run(self, ):
        menu = Menu(self.window)
        menu.run()
        pass

        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
