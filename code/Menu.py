import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Background/2/forestbridge.png')
        self.rect = self.surf.get_rect()

    def run(self,):
        pygame.mixer.music.load('./asset/Sounds/soundtrack.wav')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "Mouse Catcher", (200,200,200), ((WIN_WIDTH / 2), 200))
            self.menu_text(45, "Play Now", (17, 208, 58), ((WIN_WIDTH / 2) - 100, 270))
            self.menu_text(45, "Score", (0,10,0), ((WIN_WIDTH / 2) + 100, 270))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/Font/PixelifySans.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)