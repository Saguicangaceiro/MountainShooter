#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display

from code import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.nome = name
        self.game_mode = game_mode  # modo de jogo, se vai ser coop ou não
        self.entity_list: list[Entity] = []  # lista de entidades vazias
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        while True:
            for ent in self.entity_list: #execução das imagem em loop
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
