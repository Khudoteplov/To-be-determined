import pygame
from classes import *
from mechanics import *
# from graphics import *
from constants import *

pygame.init()

pygame.display.init()

screen = pygame.display.set_mode((screen_width, screen_height))

finished = False

character = Character()


clock = pygame.time.Clock()
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

    clock.tick(FPS)

pygame.quit()
