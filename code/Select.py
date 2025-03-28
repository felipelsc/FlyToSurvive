#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, SELECT_OPTION, C_WHITE, C_YELLOW


class Select:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/SelectBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        select_option = 0
        pygame.mixer_music.load('./asset/Select.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.select_text(50, "Fly To", C_YELLOW, ((WIN_WIDTH / 2), 70))
            self.select_text(50, "Survive", C_YELLOW, ((WIN_WIDTH / 2), 120))

            for i in range(len(SELECT_OPTION)):
                if i == select_option:
                    self.select_text(20, SELECT_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.select_text(20, SELECT_OPTION[i], C_ORANGE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if select_option < len(SELECT_OPTION) - 1:
                            select_option += 1
                        else:
                            select_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if select_option > 0:
                            select_option -= 1
                        else:
                            select_option = len(SELECT_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return SELECT_OPTION[select_option]

    def select_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)