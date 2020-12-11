import pygame
from classes import *
from mechanics import *
from graphics import *


pygame.init()

pygame.display.init()

screen = pygame.display.set_mode((400, 500))

finished = False

character = Character()

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_hero_left(character)
            elif event.key == pygame.K_RIGHT:
                move_hero_right(character)
    # FIXME: update visual
pygame.quit()
