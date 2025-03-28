#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Executor import Executor
from code.Falcon import Falcon


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Challenge1Bg':
                list_bg = []
                for i in range(5):  # challenge1bg images number
                    list_bg.append(Background(f'Challenge1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Challenge1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Challenge2Bg':
                list_bg = []
                for i in range(7):  # challenge2bg images number
                    list_bg.append(Background(f'Challenge2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Challenge2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Falcon':
                return Falcon('Falcon', (10, WIN_HEIGHT / 2 - 30))
            case 'Executor1':
                return Executor('Executor1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Executor2':
                return Executor('Executor2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
