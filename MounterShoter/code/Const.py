# aqui é o arquivo onde caso seja necessario fazer alguma modificação no projeto, seja tamanho da imagem, de alguma coisa damos prioridade por aqui
from pygame.examples.grid import WINDOW_WIDTH, WINDOW_HEIGHT

# CORES EM RGB

COLOR_BLACK = (0, 0, 0, 0)
COLOR_WHITE = (255, 255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E, determinando velocidade de cada imagem, para melhorar o fundo
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# w
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324
