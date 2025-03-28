# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_EXECUTOR = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Challenge1Bg0': 0,
    'Challenge1Bg1': 1,
    'Challenge1Bg2': 2,
    'Challenge1Bg3': 3,
    'Challenge1Bg4': 4,
    'Challenge2Bg0': 0,
    'Challenge2Bg1': 1,
    'Challenge2Bg2': 2,
    'Challenge2Bg3': 3,
    'Challenge2Bg4': 4,
    'Challenge2Bg5': 5,
    'Challenge2Bg6': 6,
    'Falcon': 3,
    'FalconShot': 3,
    'Executor1': 1,
    'Executor1Shot': 5,
    'Executor2': 1,
    'Executor2Shot': 2,
}

ENTITY_HEALTH = {
    'Challenge1Bg0': 999,
    'Challenge1Bg1': 999,
    'Challenge1Bg2': 999,
    'Challenge1Bg3': 999,
    'Challenge1Bg4': 999,
    'Challenge2Bg0': 999,
    'Challenge2Bg1': 999,
    'Challenge2Bg2': 999,
    'Challenge2Bg3': 999,
    'Challenge2Bg4': 999,
    'Challenge2Bg5': 999,
    'Challenge2Bg6': 999,
    'Falcon': 300,
    'FalconShot': 1,
    'Executor1': 50,
    'Executor1Shot': 1,
    'Executor2': 60,
    'Executor2Shot': 1,
}

ENTITY_DAMAGE = {
    'Challenge1Bg0': 0,
    'Challenge1Bg1': 0,
    'Challenge1Bg2': 0,
    'Challenge1Bg3': 0,
    'Challenge1Bg4': 0,
    'Challenge2Bg0': 0,
    'Challenge2Bg1': 0,
    'Challenge2Bg2': 0,
    'Challenge2Bg3': 0,
    'Challenge2Bg4': 0,
    'Challenge2Bg5': 0,
    'Challenge2Bg6': 0,
    'Falcon': 1,
    'FalconShot': 20,
    'Executor1': 1,
    'Executor1Shot': 20,
    'Executor2': 1,
    'Executor2Shot': 15,
}

ENTITY_SCORE = {
    'Challenge1Bg0': 0,
    'Challenge1Bg1': 0,
    'Challenge1Bg2': 0,
    'Challenge1Bg3': 0,
    'Challenge1Bg4': 0,
    'Challenge2Bg0': 0,
    'Challenge2Bg1': 0,
    'Challenge2Bg2': 0,
    'Challenge2Bg3': 0,
    'Challenge2Bg4': 0,
    'Challenge2Bg5': 0,
    'Challenge2Bg6': 0,
    'Falcon': 0,
    'FalconShot': 0,
    'Executor1': 100,
    'Executor1Shot': 0,
    'Executor2': 125,
    'Executor2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Falcon': 15,
    'Executor1': 100,
    'Executor2': 200,
}

# S
SELECT_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# P
FALCON_KEY_UP = {'Falcon': pygame.K_UP}
FALCON_KEY_DOWN = {'Falcon': pygame.K_DOWN}
FALCON_KEY_LEFT = {'Falcon': pygame.K_LEFT}
FALCON_KEY_RIGHT = {'Falcon': pygame.K_RIGHT}
FALCON_KEY_SHOOT = {'Falcon': pygame.K_RCTRL}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_CHALLENGE = 15000  # 20s
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }