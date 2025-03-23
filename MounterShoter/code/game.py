#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480)) #tamanho da janela do jogo

    def run(self,window ):
        while True:
            menu = Menu(self.window) # Aqui estou chamando o menu do jogo
            menu = menu.run()

        # Check for all events (check todos os eventos)
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
               # pygame.quit()  # close window (fecha a janela)
                #quit()  # end pygame (finaliza o pygame)
