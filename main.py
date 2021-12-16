import pygame
import sys
import random
from math import *

import physics_engine
import objects
import maps
import interface

pygame.init()
width = 1200
height = 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

physics_engine.init(display)
objects.init(display)
maps.init(display)
interface.init(display)

background = (231, 84, 128)

def close():
    pygame.quit()
    sys.exit()

def start_game(map):
    map.draw_map()

def GAME():
    map = maps.Maps()
    """название игры"""
    welcome = interface.Label(500, 100, 200, 200, None, background)
    welcome.add_text("ANGRY BIRDS", 80, "Fonts/arfmoochikncheez.ttf", (236, 240, 241))
    """кнопка, чтобы начать игру"""
    start = interface.Button(200, 400, 300, 100, start_game, (244, 208, 63), (247, 220, 111))
    start.add_text("START GAME", 60, "Fonts/arfmoochikncheez.ttf", background)
    """кнопка выхода из игры"""
    exit = interface.Button(700, 400, 300, 100, close, (241, 148, 138), (245, 183, 177))
    exit.add_text("QUIT", 60, "Fonts/arfmoochikncheez.ttf", background)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit.isActive():
                    exit.action()
                if start.isActive():
                    start_game(map)

        display.fill(background)

        start.draw()
        exit.draw()
        welcome.draw()

        pygame.display.update()
        clock.tick(60)

GAME()
