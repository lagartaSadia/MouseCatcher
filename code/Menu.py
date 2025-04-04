import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WHITE, GREEN, BLACK, MENU_OPTION, WIN_HEIGHT


class Menu:
    def __init__(self):
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.surf = pygame.image.load('./asset/Background/forestbridge.png')
        self.rect = self.surf.get_rect()

    def run(self,):
        option = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "Mouse Catcher", WHITE, ((WIN_WIDTH / 2), 200 ))

            for i in range(len(MENU_OPTION)):
                if i == option:
                    self.menu_text(45, MENU_OPTION[i], GREEN, (((WIN_WIDTH / 2) - 100) + (200 * i), 270))
                else:
                    self.menu_text(45, MENU_OPTION[i], BLACK, (((WIN_WIDTH / 2) - 100) + (200 * i), 270))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        if option < len(MENU_OPTION) - 1:
                            option += 1
                        else:
                            option = 0
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/Font/PixelifySans.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)