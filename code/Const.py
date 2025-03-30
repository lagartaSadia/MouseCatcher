import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 450

WHITE = (200, 200, 200)
GREEN = (17, 208, 58)
BLACK = (0, 10, 0)

EVENT_ENEMY = pygame.USEREVENT + 1

MENU_OPTION = ("Play Now",
               "Score")

SCORE_POS = {
    0: ((WIN_WIDTH / 2), 210),
    1: ((WIN_WIDTH / 2), 230),
    2: ((WIN_WIDTH / 2), 250),
    3: ((WIN_WIDTH / 2), 270),
    4: ((WIN_WIDTH / 2), 290),
    5: ((WIN_WIDTH / 2), 310),
    6: ((WIN_WIDTH / 2), 330),
    7: ((WIN_WIDTH / 2), 350)
}
