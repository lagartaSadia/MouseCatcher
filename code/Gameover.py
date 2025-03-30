import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.DBProxy import DBProxy
from code.Menu import Menu
from code.Score import Score


class Gameover:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Background/forestbridge.png')
        self.rect = self.surf.get_rect()

    def run(self, score):
        db_proxy = DBProxy('DBScore')

        name = ''

        score_text = Menu()
        while True:

            self.window.blit(source=self.surf, dest=self.rect)

            score_text.menu_text(30, f'Your score is {score} rats eaten', (0, 0, 0), ((WIN_WIDTH / 2), 80))

            score_text.menu_text(20, f'Enter your name to save (3 letters):', (0, 0, 0),
                                 ((WIN_WIDTH / 2), (WIN_HEIGHT / 2)))

            score_text.menu_text(20, name, (0, 0, 0), ((WIN_WIDTH / 2), (WIN_HEIGHT / 2 + 40)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 3:
                        db_proxy.save({'name': name, 'score': score})
                        Score().run()
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 3:
                            name += event.unicode

            pygame.display.flip()
