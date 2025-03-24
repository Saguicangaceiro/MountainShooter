#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):  # ABC = class abistrata
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')  # carregar a imagem
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # fazer o retangulo
        self.speed = 0

    @abstractmethod  # decoration
    def move(self, ):
        pass
