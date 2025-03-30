import pygame.image

from code.Const import WIN_WIDTH, WHITE, BLACK, SCORE_POS, WIN_HEIGHT
from code.DBProxy import DBProxy
from code.Menu import Menu


class Score:
    def __init__(self):
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.surf = pygame.image.load('./asset/Background/forestbridge.png')
        self.rect = self.surf.get_rect()

    def run(self, ):
        text = Menu()

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrive_top10()
        db_proxy.close()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            text.menu_text(70, "Top Score", BLACK, ((WIN_WIDTH / 2), 80))

            text.menu_text(30, "Name      Score", WHITE, ((WIN_WIDTH / 2), 180))

            for player_score in list_score:
                id_, name, score = player_score
                text.menu_text(20, f'{name}                      {score}', WHITE, SCORE_POS[list_score.index(player_score)])

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()