import pygame
from pygame.draw import *
import numpy as np
from constants import *
from classes import *
pygame.init()

size = 12 
spring_step_rectified = 5
spring_step_coiled = 3 


platform_surface = pygame.Surface((platform_width, platform_height), pygame.SRCALPHA)
platform_surface_moving = pygame.Surface((platform_width, platform_height), pygame.SRCALPHA)
platform_surface_disappearing = pygame.Surface((platform_width, platform_height), pygame.SRCALPHA)
platform_surface_trap = pygame.Surface((platform_width, platform_height), pygame.SRCALPHA)
spring_coiled_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
spring_rectified_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
character_turned_left_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
character_turned_right_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
platform_surface = pygame.Surface((platform_width, platform_height), pygame.SRCALPHA)
character_turned_left_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
character_turned_right_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
background_surface = pygame.Surface((screen_width, screen_height))

BROWN = (73, 50, 36)
GREEN = (1, 77, 3)
GREEN_TEA = (208, 240, 192)
YELLOW = (255, 195, 11)
BLUE = (16, 52, 166)
RED = (128, 0, 0)
ORANGE = (249, 129, 42)
GREY = (0, 0, 204)
BLACK = (255, 255, 255)

rect(platform_surface, BROWN, 
        (0, 0, platform_width, platform_height))
rect(platform_surface_moving, BLUE,
        (0, 0, platform_width, platform_height))
rect(platform_surface_disappearing, RED,
        (0, 0, platform_width, platform_height))
rect(platform_surface_trap, ORANGE,
        (0, 0, platform_width, platform_height))


line(spring_rectified_surface, BLACK, (25, 50),
        (25, 50 - spring_step_rectified))

x_current = 25
y_current = 50 - spring_step_rectified


for i in range(8):
    line(spring_rectified_surface, BLACK, (x_current, y_current),
        (25 + (-1)**i * spring_step_rectified * 2, y_current - spring_step_rectified))
    x_current = 25 + (-1)**i * spring_step_rectified * 2
    y_current = y_current - spring_step_rectified


line(spring_coiled_surface, BLACK, (25, 50),
        (25, 50 - spring_step_rectified))
x_current = 25
y_current = 50 - spring_step_rectified
for i in range(8):
    line(spring_coiled_surface, BLACK, (x_current, y_current),
        (25 + (-1)**i * spring_step_rectified * 2, y_current - spring_step_coiled))
    x_current = 25 + (-1)**i * spring_step_rectified * 2
    y_current = y_current - spring_step_coiled


rect(background_surface, GREEN_TEA, 
        (0, 0, screen_width, screen_height))


ellipse(character_turned_left_surface, YELLOW, (int(25 - size/2), 50 - size*3, size, size*3))
ellipse(character_turned_left_surface,
        YELLOW, (25 - size, 50 - size*3 + int(size/4), size, size))
polygon(character_turned_left_surface, GREEN,
# <<<<<<< HEAD
        ((25 - int(size/4), 50 - size*3), (25, 0), (25 + int(size/4), 50 - size*3)))
polygon(character_turned_left_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25 - 3*int(size/4), 0), (25 + int(size/4), 50 - size*3)))
polygon(character_turned_left_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25 + 3*int(size/4), 0), (25 + int(size/4), 50 - size*3)))


ellipse(character_turned_left_surface, YELLOW, 
        (int(25 - size/2), 50 - size*3, size, size*3))
ellipse(character_turned_left_surface,
        YELLOW, (25, 50 - size*3+ int(size/4), size, size))
polygon(character_turned_left_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25, 0), (25 + int(size/4), 50 - size*3)))
polygon(character_turned_left_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25 - 3*int(size/4), 0), (25 + int(size/4), 50 - size*3)))
polygon(character_turned_left_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25 + 3*int(size/4), 0), (25 + int(size/4), 50 - size*3)))
polygon(character_turned_left_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25 - 3*int(size/4), 50), (25 + int(size/4), 50 - size*3)))
polygon(character_turned_left_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25, 50), (25 + int(size/4), 50 - size*3)))


ellipse(character_turned_right_surface, YELLOW,
        (int(25 - size/2), 50 - size*3, size, size*3))
ellipse(character_turned_right_surface, YELLOW, (25, 50 - size*3+ int(size/4), size, size))
polygon(character_turned_right_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25, 50), (25 + int(size/4), 50 - size*3)))
polygon(character_turned_right_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25 - 3*int(size/4), 50), (25 + int(size/4), 50 - size*3)))
polygon(character_turned_right_surface, GREEN,
        ((25 - int(size/4), 50 - size*3), (25, 50), (25 + int(size/4), 50 - size*3)))

