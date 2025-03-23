#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))  # tamanho da janela do jogo

    def run(self):

        while True:
            menu = Menu(self.window)  # Aqui estou chamando o menu do jogo
            menu.run()
            pass