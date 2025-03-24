#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_BLACK, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png")  # pagamos a imagem
        self.rect = self.surf.get_rect(left=0, top=0)  # criamos o retangulo para a imagem

    def run(self, ):

        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # ao colocar o paramentro -1 a musica sempre que acaba ela recomeça
        while True:
            # DRAW IMAGE (TODAS AS IMAGENS)

            #FUNDO

            self.window.blit(source=self.surf, dest=self.rect)  # falamos q a imagem tem que aparecer no rentangulo
            self.menu_text(50, 'mountain', (COLOR_BLACK), ((WINDOW_WIDTH / 2), 70))
            self.menu_text(50, 'Shoter', (COLOR_BLACK), ((WINDOW_WIDTH / 2), 120))

            #TEXTOS

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, (MENU_OPTION[i]), COLOR_YELLOW, ((WINDOW_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, (MENU_OPTION[i]), COLOR_WHITE, ((WINDOW_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()  # mostramos a imagem (atualizando a tela)

            # check for all events #funcionabilidade para não congela a tela e para poder fecha o game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Encerra o Pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        # Move para baixo no menu
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0  # Volta para a primeira opção, se estiver na última

                    if event.key == pygame.K_UP:  # UP KEY
                        # Move para cima no menu
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucidasanstypewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
