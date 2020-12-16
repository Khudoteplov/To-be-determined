import pygame
from classes import *
from mechanics import *
# from graphics import *
from constants import *
from platform_generator import *

pygame.init()

pygame.display.init()

screen = pygame.display.set_mode((screen_width, screen_height))

finished = False

character = Character()

clock = pygame.time.Clock()

height = 0
platforms = []
top_generated_level = 10 * screen_height
platforms += generate_platforms(0, 10 * screen_height)

while not finished:
    move_hero(character, 1)
    for platform in platforms:
        if check_bounce(character, platform):
            bounce(character, platform)
            height = platform.y
            break

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
