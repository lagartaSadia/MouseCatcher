import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        pygame.mixer.music.load('./asset/Sounds/soundtrack.wav')
        pygame.mixer.music.play(-1)

        while True:
            menu = Menu()
            menu_return = menu.run()
            print(f'menu option {menu_return}')

            if menu_return == 'Play Now':
                level = Level(self.window, 'Level 1')
                level.run()
            elif menu_return == 'Score':
                score = Score()
                score.run()
