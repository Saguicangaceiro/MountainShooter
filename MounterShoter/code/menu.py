#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_ORANGE, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png")  # pagamos a imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # criamos o retangulo para a imagem

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # ao colocar o paramentro -1 a musica sempre que acaba ela recomeça
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # falamos q a imagem tem que aparecer no rentangulo
            self.menu_text(50, 'mountain', (COLOR_ORANGE), ((WINDOW_WIDTH / 2), 70))
            self.menu_text(50, 'Shoter', (COLOR_ORANGE), ((WINDOW_WIDTH / 2) , 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, (MENU_OPTION[i]), C_WHITE, ((WINDOW_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()  # mostramos a imagem (atualizando a tela)

            # check for all events #funcionabilidade para não congela a tela e para poder fecha o game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucidasanstypewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
