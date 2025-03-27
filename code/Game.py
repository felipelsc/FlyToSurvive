#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, SELECT_OPTION
from code.Challenge import Challenge
from code.Select import Select
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            select = Select(self.window)
            select_return = select.run()

            if select_return in [SELECT_OPTION[0]]:
                falcon_score = [0]
                challenge = Challenge(self.window, 'Challenge1', select_return, falcon_score)
                challenge_return = challenge.run(falcon_score)
                if challenge_return:
                    challenge = Challenge(self.window, 'Challenge2', select_return, falcon_score)
                    challenge_return = challenge.run(falcon_score)
                    if challenge_return:
                        score.save(select_return, falcon_score)

                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()